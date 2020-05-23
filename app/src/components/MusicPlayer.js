import React, {useState, useEffect} from 'react';
import Navbar from "react-bootstrap/Navbar";
import RangeSlider from 'react-bootstrap-range-slider';
import Nav from "react-bootstrap/Nav";
import {faStepForward, faStepBackward} from "@fortawesome/free-solid-svg-icons";
import {faPauseCircle} from "@fortawesome/free-regular-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";


function MusicPlayer() {

    const [ progress, setProgress ] = useState(0);
    const [ duration, setDuration ] = useState(60);
    const [ songName, setSongName ] = useState("Loading");
    const [ isPlaying, setIsPlaying ] = useState(false);

    useEffect(() => {
        fetch('/api/songinfo').then(res => res.json()).then(data => {
            if (data.authorized) {
                setSongName(data.name);
                setDuration(Math.round(data.duration / 1000));
                setIsPlaying(data.playing);
            } else {
                setSongName("Sign into Spotify");
            }
        });
    }, []);
    console.log(duration);
    console.log(isPlaying);

    return (
        <>
            <Navbar fixed={'bottom'} variant={'dark'} bg={'dark'} style={{'flexFlow':'column'}}>
                <Navbar.Brand style={{'marginRight':'0px'}}> {songName} </Navbar.Brand>
                <Nav style={{'fontSize':'32px'}}>
                    <Nav.Link style={{'padding':'0px', 'marginTop':'-10px', 'marginBottom':'-10px'}}>
                        <FontAwesomeIcon icon={faPauseCircle} />
                    </Nav.Link>
                </Nav>
                <Nav style={{'fontSize': 'larger', 'height':'25px'}}>
                    <Nav.Link style={{'marginTop':'-2px'}}><FontAwesomeIcon icon={faStepBackward} /></Nav.Link>
                    <div style={{'width':'80vw'}}>
                        <RangeSlider
                            tooltip={'off'}
                            variant={'primary'}
                            value={progress}
                            onChange={changeEvent => setProgress(changeEvent.target.value)}
                        />
                    </div>
                    <Nav.Link style={{'marginTop':'-2px'}}><FontAwesomeIcon icon={faStepForward} /></Nav.Link>
                </Nav>
                <Navbar.Text style={{'padding':'0px'}}>1:20 / 2:30</Navbar.Text>
            </Navbar>
        </>
    );
}

export default MusicPlayer;
