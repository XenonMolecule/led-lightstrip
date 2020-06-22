import React, {useState, useEffect} from 'react';
import ColorSlider from "./ColorSlider";
import ColorButton from "./ColorButton";
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import AlphaSlider from "./AlphaSlider";

function hexToRgb(hex) {
    let result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16)
    } : null;
}

function ColorSelector(props) {
    const [alpha, setAlpha] = useState(1.0);

    useEffect(() => {
        props.emitColor({
            red: Math.floor(props.color.r * alpha),
            green: Math.floor(props.color.g * alpha),
            blue: Math.floor(props.color.b * alpha)
        });
    },[props.color])

    function rgbToRgba(rgb) {
        return "rgba(" + rgb.r + "," + rgb.g + "," + rgb.b + "," + alpha + ")";
    }

    const colorsRow1 = ["#ff0000", "#ff7f00", "#ffff00", "#00ff00"];
    const colorsRow2 = ["#00ffff", "#0000ff", "#7f00ff", "#ff00ff"];
    const colorsRow3 = ["#000000", "#ffffff"];

    function buildRowFromColors(colors) {
        let row = [];
        colors.forEach((color) => {
            row.push(
                <Col>
                    <ColorButton
                        color={color}
                        onClick = {(newColor) => {
                            props.setColor(hexToRgb(newColor));
                        }}
                    />
                </Col>
            );
        });
        return row;
    }

    const buttonsRow1 = buildRowFromColors(colorsRow1);
    const buttonsRow2 = buildRowFromColors(colorsRow2);
    const buttonsRow3 = buildRowFromColors(colorsRow3);

    return (
        <>
            <ColorSlider color={rgbToRgba(props.color)}
                onChange={(newColor) => {
                    props.setColor(newColor.rgb);
                }}/>
            <Container>
                <Row style={{"marginTop":'10px'}}>
                    {buttonsRow1}
                </Row>
                <Row style={{"marginTop":'10px'}}>
                    {buttonsRow2}
                </Row>
                <Row style={{"marginTop":'10px'}}>
                    {buttonsRow3}
                    <Col xs={6}>
                        <AlphaSlider color={rgbToRgba(props.color)}
                            onChange = {(newColor) => {
                                setAlpha(newColor.rgb.a);
                                props.setColor(newColor.rgb);
                            }}/>
                    </Col>
                </Row>
            </Container>
        </>
    )
}

export default ColorSelector;
