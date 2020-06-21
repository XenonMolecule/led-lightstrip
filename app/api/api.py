import time
import json
import multiprocessing
import os
import spotipy
from flask import Flask, request, session, redirect
from flask_socketio import SocketIO, emit
from flask_pymongo import PyMongo
from dotenv import load_dotenv

# Load Spotify Credentials from .env
load_dotenv()

app = Flask('api')
app.secret_key = os.getenv("FLASK_SECRET_KEY")
app.config["MONGO_URI"] = "mongodb://localhost:27017/lightdb"
mongo = PyMongo(app)
socketio = SocketIO(app)
settings = None
lock = None

# Initialize spotify api variables
SPOT_CLI_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOT_CLI_SEC = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOT_REDIRECT_URI = "http://10.0.0.209/api/auth_callback"
SPOT_SCOPE = 'user-read-playback-state,user-modify-playback-state,user-read-currently-playing'

@app.route('/api/time')
def get_current_time():
    return json.dumps({'time': time.time()})

@app.route('/api/auth')
def auth():
    # According to Stack Overflow (famous last words) it is safest to recreate
    # SpotifyOAuth objects each time you need to use them so you don't leak tokens
    sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id = SPOT_CLI_ID, \
                                            client_secret = SPOT_CLI_SEC, \
                                            redirect_uri = SPOT_REDIRECT_URI, \
                                            scope = SPOT_SCOPE)
    return redirect(sp_oauth.get_authorize_url())

@app.route('/api/auth_callback')
def auth_callback():
    sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id = SPOT_CLI_ID, \
                                            client_secret = SPOT_CLI_SEC, \
                                            redirect_uri = SPOT_REDIRECT_URI, \
                                            scope = SPOT_SCOPE)
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code, check_cache=False)

    #Save the token info to this specific users session
    session['token_info'] = token_info
    return redirect('/')

@app.route('/api/test_spotify')
def test_spotify():
    session['token_info'], authorized = get_token(session)
    session.modified = True
    if not authorized:
        return redirect('/api/auth')
    sp = spotipy.Spotify(auth=session.get('token_info').get('access_token'))
    return json.dumps({'curr_song': sp.current_user_playing_track()})

@app.route('/api/songinfo')
def songinfo():
    session['token_info'], authorized = get_token(session)
    session.modified = True
    if not authorized:
        return json.dumps({'authorized':False})
    timestamp = time.time()
    sp = spotipy.Spotify(auth=session.get('token_info').get('access_token'))
    timestamp += ((timestamp - time.time()) / 2)
    timestamp = round(timestamp * 1000)
    song_data = sp.current_playback()
    return json.dumps({
        'authorized':True,
        'spotify_timestamp': song_data['timestamp'],
        'calc_timestamp': int(timestamp),
        'progress': song_data['progress_ms'],
        'name': song_data['item']['name'],
        'duration': song_data['item']['duration_ms'],
        'playing': song_data['is_playing']
    })

@app.route('/api/pause_playback', methods=['PUT'])
def pause():
    session['token_info'], authorized = get_token(session)
    session.modified = True
    if not authorized:
        return json.dumps({'success':False})
    sp = spotipy.Spotify(auth=session.get('token_info').get('access_token'))
    sp.pause_playback()
    return json.dumps({'success':True})

@app.route('/api/start_playback', methods=['PUT'])
def play():
    session['token_info'], authorized = get_token(session)
    session.modified = True
    if not authorized:
        return json.dumps({'success':False})
    sp = spotipy.Spotify(auth=session.get('token_info').get('access_token'))
    sp.start_playback()
    return json.dumps({'success':True})

@app.route('/api/seek_playback', methods=['PUT'])
def seek():
    session['token_info'], authorized = get_token(session)
    session.modified = True
    if not authorized:
        return json.dumps({'success':False})
    progress_ms = request.get_json()['progress']
    sp = spotipy.Spotify(auth=session.get('token_info').get('access_token'))
    sp.seek_track(progress_ms)
    return json.dumps({'success':True})

@app.route('/api/previous_track', methods=['PUT'])
def previous_track():
    session['token_info'], authorized = get_token(session)
    session.modified = True
    if not authorized:
        return json.dumps({'success':False})
    sp = spotipy.Spotify(auth=session.get('token_info').get('access_token'))
    sp.previous_track()
    return json.dumps({'success':True})

@app.route('/api/next_track', methods=['PUT'])
def next_track():
    session['token_info'], authorized = get_token(session)
    session.modified = True
    if not authorized:
        return json.dumps({'success':False})
    sp = spotipy.Spotify(auth=session.get('token_info').get('access_token'))
    sp.next_track()
    return json.dumps({'success':True})

# Get the spotify token of the user for this session and check if they are authenticated
def get_token(session):
    token_valid = False
    token_info = session.get('token_info', {})

    #If the session does not have a token then break out as unauthenticated
    if not (session.get('token_info', False)):
        return token_info, token_valid

    #Check if the token has expired
    now = int(time.time())
    is_token_expired = token_info.get('expires_at') - now < 60

    #Refresh token if it has expired
    if (is_token_expired):
        sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id = SPOT_CLI_ID, \
                                            client_secret = SPOT_CLI_SEC, \
                                            redirect_uri = SPOT_REDIRECT_URI, \
                                            scope = SPOT_SCOPE)
        token_info = sp_oauth.refresh_access_token(token_info.get('refresh_token'))

    token_valid = True
    return token_info, token_valid

@app.route('/api/change_pattern', methods=['POST'])
def change_pattern():
    req = request.get_json()
    pattern = str(req['pattern'])
    if len(pattern) > 10:
        pattern = pattern[:10]
    with lock:
        settings.queue_patt = pattern
        settings.hold_patt = req['hold'] == "True"
    return json.dumps({'success': 'success'})

@socketio.on('setcolor')
def set_color(message):
    with lock:
        settings.back_red = int(message['red']) // 2
        settings.back_green = int(message['green']) // 2
        settings.back_blue = int(message['blue']) // 2
        settings.fore_red = int(message['red'])
        settings.fore_green = int(message['green'])
        settings.fore_blue = int(message['blue'])

@socketio.on('connect')
def connect():
    print("New Connection")
    #test_col = mongo.db["testcol"]
    #print(test_col.find_one())

@socketio.on('disconnect')
def disconnect():
    print("Client disconnected")

def run_server(settings_link, read_lock):
    global settings
    global lock
    settings = settings_link
    lock = read_lock
    #test_col = mongo.db["testcol"]
    #test_col.insert_one({"test": "testing", "test2": "still testing"})
    socketio.run(app, host='127.0.0.1', port='5000', debug=False, use_reloader=False)

if __name__ == "__main__":
    run_server(multiprocessing.Manager().Namespace(), multiprocessing.Lock())
