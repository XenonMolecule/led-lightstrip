import React, {useState, useEffect} from 'react';
import socketIOClient from 'socket.io-client';
import ColorSelector from "./colorselector/ColorSelector";
import PulseButton from "./PulseButton";
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';
import Button from 'react-bootstrap/Button';
import {faLink, faUnlink} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";

const ENDPOINT = "/"

function LightDJ() {
    const [socket, setSocket] = useState(null);
    const [backColor, setBackColor] = useState({r: '0', g: '0', b:'0'});
    const [foreColor, setForeColor] = useState({r: '0', g: '0', b:'0'});
    const [linkColors, setLinkColors] = useState(false);

    useEffect(() => {
        setSocket(socketIOClient(ENDPOINT));
    }, []);

    return (
        <>
            <Card>
                <Card.Header>
                    <Row>
                        <Col>
                            Background Color
                        </Col>
                        <Col>
                            <Row style = {{'justifyContent':'flex-end', 'paddingRight':'6px'}}>
                                <Button style={{'width': '25px', 'height': '25px', 'border':'1px solid rgba(0,0,0,.125)'}}
                                        variant={'light'}
                                        onClick = {() => {
                                            setLinkColors(!linkColors);
                                            setForeColor(backColor);
                                        }}
                                >
                                    <FontAwesomeIcon icon={linkColors ? faLink : faUnlink} style={{
                                        'marginLeft':'-7.5px',
                                        'marginBottom':'4px',
                                        'paddingBottom': '4px'
                                    }}/>
                                </Button>
                            </Row>
                        </Col>
                    </Row>
                </Card.Header>
                <ListGroup variant="flush">
                    <ListGroup.Item>
                        <ColorSelector emitColor = {(color) => {
                            if(socket != null) {
                                socket.emit('set_background_color', color);
                            }
                        }}
                        setColor = {(color) => {
                            setBackColor(color);
                        }}
                        color = {backColor}/>
                    </ListGroup.Item>
                </ListGroup>
            </Card>
            <Card style = {{'marginTop': '10px'}}>
                <Card.Header>
                    <Row>
                        <Col>
                            Foreground Color
                        </Col>
                        <Col>
                            <Row style = {{'justifyContent':'flex-end', 'paddingRight':'6px'}}>
                                <Button style={{'width': '25px', 'height': '25px', 'border':'1px solid rgba(0,0,0,.125)'}}
                                        variant={'light'}
                                        onClick = {() => {
                                            if (linkColors) {
                                                setForeColor(backColor);
                                            } else {
                                                setBackColor(foreColor);
                                            }
                                            setLinkColors(!linkColors);
                                        }}
                                >
                                    <FontAwesomeIcon icon={linkColors ? faLink : faUnlink} style={{
                                        'marginLeft':'-7.5px',
                                        'marginBottom':'4px',
                                        'paddingBottom': '4px'
                                    }}/>
                                </Button>
                            </Row>
                        </Col>
                    </Row>
                </Card.Header>
                <ListGroup variant="flush">
                    <ListGroup.Item>
                        <ColorSelector emitColor = {(color) => {
                            if(socket != null) {
                                socket.emit('set_foreground_color', color);
                            }
                        }}
                        setColor = {(color) => {
                            if (linkColors) {
                                setBackColor(color);
                            } else {
                                setForeColor(color);
                            }
                        }}
                        color = {linkColors ? backColor : foreColor}/>
                    </ListGroup.Item>
                </ListGroup>
            </Card>
            <Container>
                <Row style={{"marginTop":'10px'}}>
                    <PulseButton/>
                </Row>
            </Container>
        </>
    );
}

export default LightDJ;
