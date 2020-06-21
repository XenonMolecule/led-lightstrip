import React from 'react';
import Button from 'react-bootstrap/Button';
import {faSun} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";

function PulseButton() {
    return (
        <Button
            variant="dark"
            block
            size = 'lg'
            onClick = {() => {
                const body = JSON.stringify({
                    pattern: 'pulse',
                    hold: false
                });

                fetch('/api/change_pattern', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: body})
                    .then(res => res.json())
                    .then(data => console.log(data))
                    .catch(error => console.error('Error:', error));
            }}
        >
            <FontAwesomeIcon icon={faSun}/>
        </Button>
    )
}

export default PulseButton;
