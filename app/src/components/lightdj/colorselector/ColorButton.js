import React from 'react';
import Button from 'react-bootstrap/Button';

function ColorButton(props) {
    return (
        <Button
            variant="secondary"
            style={{"backgroundColor": props.color, "width": "100%", "height": "25px"}}
            onClick = {() => {
                props.onClick(props.color);
            }}
        />
    )
}

export default ColorButton;
