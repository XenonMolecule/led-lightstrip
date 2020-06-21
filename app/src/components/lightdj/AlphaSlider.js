import React from 'react';
import { AlphaPicker } from 'react-color'
import ThickSliderPointer from "./ThickSliderPointer";

function AlphaSlider(props) {
    return (
        <>
            <AlphaPicker
                color = {props.color}
                onChange = {(color) => {props.onChange(color);}}
                width = {"100%"}
                height = {"100%"}
                pointer = {ThickSliderPointer}
            />
        </>
    )
}

export default AlphaSlider;
