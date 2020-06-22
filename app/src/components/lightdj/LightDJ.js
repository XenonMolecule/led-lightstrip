import React, {useState, useEffect} from 'react';
import socketIOClient from 'socket.io-client';
import ColorSelector from "./colorselector/ColorSelector";
import PulseButton from "./PulseButton";
import Row from 'react-bootstrap/Row';
import Container from 'react-bootstrap/Container';
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';

const ENDPOINT = "/"

function LightDJ() {
    const [socket, setSocket] = useState(null);

    useEffect(() => {
        setSocket(socketIOClient(ENDPOINT));
    }, []);

    return (
        <>
            <Card>
                <Card.Header>Background Color</Card.Header>
                <ListGroup variant="flush">
                    <ListGroup.Item>
                        <ColorSelector updateColor = {(color) => {
                            socket.emit('set_background_color', color);
                        }}/>
                    </ListGroup.Item>
                </ListGroup>
            </Card>
            <Card style = {{'marginTop': '10px'}}>
                <Card.Header>Foreground Color</Card.Header>
                <ListGroup variant="flush">
                    <ListGroup.Item>
                        <ColorSelector updateColor = {(color) => {
                            socket.emit('set_foreground_color', color);
                        }}/>
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
