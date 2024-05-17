import React, { useEffect, useState } from 'react';
import AuthController from './controllers/AuthController';
import AppController from './controllers/AppController';

function App() {
  const [ content, setContent] = useState();
  const [ auth, setAuth] = useState(false);

  useEffect(() => {
    const authToken = localStorage.getItem('authToken');
    
    if (authToken) {
      setContent(<AppController />);
    } else {
      setContent(<AuthController setAuth={setAuth} />);
    }
  }, [auth]);

  return content;
}

export default App;
