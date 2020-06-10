import React, {useState, useEffect} from 'react';
import Navbar from "react-bootstrap/Navbar";
import RangeSlider from 'react-bootstrap-range-slider';
import Nav from "react-bootstrap/Nav";
import {faStepForward, faStepBackward} from "@fortawesome/free-solid-svg-icons";
import {faPauseCircle, faPlayCircle} from "@fortawesome/free-regular-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";

function fmtSecs(seconds) {
    let secs = seconds % 60;
    const mins = Math.floor(seconds / 60);
    if (secs < 10) {
        secs = "0" + secs;
    }
    return mins + ":" + secs;
}

function MusicPlayer() {

    const [ progress, setProgress ] = useState(0);
    const [ visProgress, setVisProgress ] = useState(0);
    const [ bindProgress, setBindProgress ] = useState(true);
    const [ duration, setDuration ] = useState(60);
    const [ songName, setSongName ] = useState("Loading");
    const [ isPlaying, setIsPlaying ] = useState(false);
    const [ startTime, setStartTime ] = useState(Date.now());
    const [ updateSong, setUpdateSong ] = useState(true);
    const [ checkTime, setCheckTime ] = useState(Date.now());

    function seekPlayback() {
        fetch('/api/seek_playback', {
            method:"PUT",
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                "progress": visProgress * 1000,
            })}).then(res => res.json()).then(data => {
                setTimeout(() => {
                    setBindProgress(true);
                }, 1000);
                setUpdateSong(true);
            }
        );
    }

    function forceUpdate() {
        setUpdateSong(true);
    }

    useEffect(() => {
        if (updateSong) {
            fetch('/api/songinfo').then(res => res.json()).then(data => {
                if (data.authorized) {
                    setSongName(data.name);
                    setDuration(Math.round(data.duration / 1000));
                    setIsPlaying(data.playing);
                    setStartTime(data.calc_timestamp - data.progress);
                    const curr_progress = (Date.now() - data.calc_timestamp) + data.progress;
                    const ceil_progress = Math.ceil(curr_progress / 1000) * 1000;
                    setVisProgress(Math.round(curr_progress / 1000));
                    setTimeout(() => {
                        setProgress(ceil_progress / 1000);
                    }, ceil_progress - curr_progress);
                } else {
                    setSongName("Sign into Spotify");
                }
            });
            setUpdateSong(false);
        }
    }, [updateSong]);

    useEffect(() => {
        if(isPlaying) {
            const offset = Date.now() - startTime;
            let inc_progress = setTimeout(() => {
                if (progress >= duration) {
                    setUpdateSong(true);
                }
                setProgress(progress + 1);
            }, (Math.ceil(offset / 1000) * 1000) - offset);
            return () => clearTimeout(inc_progress);
        }
    }, [progress, isPlaying, duration, startTime]);

    useEffect(() => {
        if (bindProgress) {
            setVisProgress(progress);
        }
    }, [progress, bindProgress]);

    useEffect(() => {
        window.addEventListener('focus', forceUpdate);
        let check_sync = setInterval(() => {
            if (Date.now() - checkTime > 2000) {
                forceUpdate();
            }
            setCheckTime(Date.now())
        }, 1000);
        return () => {
            window.removeEventListener('focus', forceUpdate);
            clearInterval(check_sync);
        }
    }, []);

    return (
        <>
            <Navbar fixed={'bottom'} variant={'dark'} bg={'dark'} style={{'flexFlow':'column'}}>
                <Navbar.Brand style={{'marginRight':'0px'}}> {songName} </Navbar.Brand>
                <Nav style={{'fontSize':'32px'}}>
                    <Nav.Link style={{'padding':'0px', 'marginTop':'-10px', 'marginBottom':'-10px'}}>
                        <FontAwesomeIcon icon={(isPlaying) ? faPauseCircle : faPlayCircle} onClick = {() => {
                            if (isPlaying) {
                                fetch('/api/pause_playback', {method:"PUT"});
                            } else {
                                fetch('/api/start_playback', {method:"PUT"});
                                setUpdateSong(true);
                            }
                            setIsPlaying(!isPlaying);
                        }} />
                    </Nav.Link>
                </Nav>
                <Nav style={{'fontSize': 'larger', 'height':'25px'}}>
                    <Nav.Link style={{'marginTop':'-2px'}}><FontAwesomeIcon icon={faStepBackward} onClick={() => {
                        fetch('/api/previous_track', {method:'PUT'});
                        setUpdateSong(true);
                    }}/></Nav.Link>
                    <div style={{'width':'80vw'}}
                            onMouseUp={seekPlayback}
                            onTouchEnd={seekPlayback}>
                        <RangeSlider
                            tooltip={'off'}
                            variant={'primary'}
                            max={duration}
                            value={visProgress}
                            onChange={(changeEvent) => {
                                setBindProgress(false);
                                setVisProgress(parseInt(changeEvent.target.value))
                            }}
                        />
                    </div>
                    <Nav.Link style={{'marginTop':'-2px'}}><FontAwesomeIcon icon={faStepForward} onClick={() => {
                        fetch('/api/next_track', {method:'PUT'});
                        setUpdateSong(true);
                    }}/></Nav.Link>
                </Nav>
                <Navbar.Text style={{'padding':'0px'}}>{fmtSecs(visProgress) + " / " + fmtSecs(duration)}</Navbar.Text>
            </Navbar>
        </>
    );
}

export default MusicPlayer;
