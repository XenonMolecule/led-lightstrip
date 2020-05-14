import React, {useState, useEffect} from 'react';
import Container from 'react-bootstrap/Container';
import socketIOClient from 'socket.io-client';
import { ChromePicker } from 'react-color'

const ENDPOINT = "/"

function App() {
  const [currentTime, setCurrentTime] = useState(0);
  const [color, setColor] = useState("#000000");
  const [socket, setSocket] = useState(null);

  useEffect(() => {
    fetch('/api/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });

    setSocket(socketIOClient(ENDPOINT));
  }, []);

  return (
      <Container>
          <p>The current time is {currentTime}.</p>
          <ChromePicker disableAlpha={true}
                  color = {color}
                  onChange={(color) => {
              socket.emit('setcolor', {red: color.rgb.r, green: color.rgb.g, blue: color.rgb.b});
              setColor(color);
          }}/>
      </Container>
  );
}

export default App;
