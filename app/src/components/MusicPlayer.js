import React, {useState} from 'react';
import Navbar from "react-bootstrap/Navbar";
import RangeSlider from 'react-bootstrap-range-slider';
import Nav from "react-bootstrap/Nav";
import {faStepForward, faStepBackward} from "@fortawesome/free-solid-svg-icons";
import {faPauseCircle} from "@fortawesome/free-regular-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";


function MusicPlayer() {

    const [ value, setValue ] = useState(0);

    return (
        <>
            <Navbar fixed={'bottom'} variant={'dark'} bg={'dark'} style={{'flexFlow':'column'}}>
                <Navbar.Brand style={{'marginRight':'0px'}}>DJ Got Us Fallin' in Love</Navbar.Brand>
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
                            value={value}
                            onChange={changeEvent => setValue(changeEvent.target.value)}
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
