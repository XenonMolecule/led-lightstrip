import React, {useState, useEffect} from 'react';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
import socketIOClient from 'socket.io-client';

const ENDPOINT = "/"

function App() {
  const [currentTime, setCurrentTime] = useState(0);
  const [redVal, setRedVal] = useState(0);
  const [blueVal, setBlueVal] = useState(0);
  const [greenVal, setGreenVal] = useState(0);
  const [socket, setSocket] = useState(null);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
    
    setSocket(socketIOClient(ENDPOINT));
  }, []);

  return (
      <Container>
        <p>The current time is {currentTime}.</p>
        <div style={{'height': '250px', 'width': '250px', 'backgroundColor':'rgb(' + redVal + ',' + greenVal + ',' + blueVal + ')'}}/>
        <br/>
        <p>
          <input type={'range'} min={'0'} max={'255'} value={redVal} onChange = {(e) => {
            setRedVal(parseInt(e.target.value));
            socket.emit('setcolor', {red: e.target.value, green: greenVal, blue: blueVal});
          }}/>
          {'  Red: ' + redVal}
        </p>
        <br/>
        <p>
          <input type={'range'} min={'0'} max={'255'} value={greenVal} onChange = {(e) => {
            setGreenVal(parseInt(e.target.value));
            socket.emit('setcolor', {red: redVal, green: e.target.value, blue: blueVal});
          }}/>
          {'  Green: ' + greenVal}
        </p>
        <br/>
        <p>
          <input type={'range'} min={'0'} max={'255'} value={blueVal} onChange = {(e) => {
            setBlueVal(parseInt(e.target.value));
            socket.emit('setcolor', {red: redVal, green: greenVal, blue: e.target.value});
          }}/>
          {'  Blue: ' + blueVal}
        </p>
      </Container>
  );
}

export default App;
