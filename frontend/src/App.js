import React, { useState } from 'react';
import AuthController from './controllers/AuthController';

function App() {
  const [ authToken ] = useState(null);

  return (
    (
      authToken ? 
        <div>
          Hola
        </div>
      :
        <AuthController />
    )
  );
}

export default App;
