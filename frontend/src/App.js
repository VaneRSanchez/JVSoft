import React, { useEffect, useState } from 'react';
import AuthController from './controllers/AuthController';
import AppController from './controllers/AppController';

function App() {
  const [ auth, setAuth] = useState(false);

  useEffect(() => {
    const authToken = localStorage.getItem('authToken');
    
    if (authToken) {
      setAuth(true);
    } else {
      setAuth(false);
    }
  }, []);

  return (
    (
      auth ? 
        <AppController />
      :
        <AuthController setAuth={setAuth} />
    )
  );
}

export default App;
