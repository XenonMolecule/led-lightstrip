import React, {useState, useEffect} from 'react';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';

function updateColor(red, green, blue) {
  const body = JSON.stringify({
    red: red,
    green: green,
    blue: blue
  });

  fetch('/setcolor', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: body})
      .then(res => res.json())
      .then(data => console.log(data))
      .catch(error => console.error('Error:', error));
}

function App() {
  const [currentTime, setCurrentTime] = useState(0);
  const [redVal, setRedVal] = useState(0);
  const [blueVal, setBlueVal] = useState(0);
  const [greenVal, setGreenVal] = useState(0);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  return (
      <Container>
        <p>The current time is {currentTime}.</p>
        <div style={{'height': '250px', 'width': '250px', 'backgroundColor':'rgb(' + redVal + ',' + greenVal + ',' + blueVal + ')'}}/>
        <br/>
        <p>
          <input type={'range'} min={'0'} max={'255'} value={redVal} onChange = {(e) => {
            setRedVal(parseInt(e.target.value));
          }}/>
          {'  Red: ' + redVal}
        </p>
        <br/>
        <p>
          <input type={'range'} min={'0'} max={'255'} value={greenVal} onChange = {(e) => {
            setGreenVal(parseInt(e.target.value));
          }}/>
          {'  Green: ' + greenVal}
        </p>
        <br/>
        <p>
          <input type={'range'} min={'0'} max={'255'} value={blueVal} onChange = {(e) => {
            setBlueVal(parseInt(e.target.value));
          }}/>
          {'  Blue: ' + blueVal}
        </p>
        <br/>
        <Button variant="primary" onClick = {() => {updateColor(redVal, greenVal, blueVal)}}>Update</Button>
      </Container>
  );
}

export default App;
