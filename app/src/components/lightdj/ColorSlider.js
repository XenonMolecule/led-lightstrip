import React from 'react';
import { HuePicker } from 'react-color'

function ColorSlider(props) {
    return (
        <>
            <HuePicker
                color = {props.color}
                onChange = {(color) => {props.onChange(color)}}
                width = {"100%"}
            />
        </>
    )
}

export default ColorSlider;
