import React, {useState, useEffect} from 'react';
import Container from 'react-bootstrap/Container';
import MusicPlayer from "./components/MusicPlayer";
import LightDJ from "./components/lightdj/LightDJ";

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/api/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  return (
      <>
          <Container>
              <p>The current time is {currentTime}.</p>
              <LightDJ/>
          </Container>
          <MusicPlayer/>
      </>
  );
}

export default App;
