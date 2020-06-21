import React, {useState, useEffect} from 'react';
import ColorSlider from "./ColorSlider";
import socketIOClient from 'socket.io-client';
import ColorButton from "./ColorButton";
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import PulseButton from "./PulseButton";

const ENDPOINT = "/"

function hexToRgb(hex) {
    let result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16)
    } : null;
}

function LightDJ() {
    const [color, setColor] = useState("#000000");
    const [socket, setSocket] = useState(null);

    function updateColor(hex, rgb) {
        socket.emit('setcolor', {red: rgb.r, green: rgb.g, blue: rgb.b});
        setColor(hex);
    }

    useEffect(() => {
        setSocket(socketIOClient(ENDPOINT));
    }, []);

    const colorsRow1 = ["#ff0000", "#ff7f00", "#ffff00", "#00ff00"];
    const colorsRow2 = ["#00ffff", "#0000ff", "#7f00ff", "#ff00ff"];

    function buildRowFromColors(colors) {
        let row = [];
        colors.forEach((color) => {
            row.push(
                <Col>
                    <ColorButton
                        color={color}
                        onClick = {(newColor) => {
                            updateColor(newColor, hexToRgb(newColor));
                        }}
                    />
                </Col>
            );
        });
        return row;
    }

    const buttonsRow1 = buildRowFromColors(colorsRow1);
    const buttonsRow2 = buildRowFromColors(colorsRow2);

    return (
        <>
            <ColorSlider color={color}
                onChange={(newColor) => {
                    updateColor(newColor.hex, newColor.rgb);
                }}/>
            <Container>
                <Row style={{"marginTop":'10px'}}>
                    {buttonsRow1}
                </Row>
                <Row style={{"marginTop":'10px'}}>
                    {buttonsRow2}
                </Row>
                <Row style={{"marginTop":'10px'}}>
                    <PulseButton/>
                </Row>
            </Container>
        </>
    )
}

export default LightDJ;
