import React, { useState } from 'react';
import AuthController from './controllers/AuthController';
import AppController from './controllers/AppController';

function App() {
  const [ authToken ] = useState(true);

  return (
    (
      authToken ? 
        <AppController />
      :
        <AuthController />
    )
  );
}

export default App;
