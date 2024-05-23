import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link, Navigate } from 'react-router-dom';
import { v4 as uuidv4 } from 'uuid';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faTimesCircle } from '@fortawesome/free-regular-svg-icons'
import logo2 from '../assets/images/logo4.png';
import SignIn from '../components/auth/SignIn';
import Alert from '../components/Alert';
import SignUp from '../components/auth/SignUp';

function AuthController({ setAuth }) {
  const [modals, setModals] = useState([]);
  const [alerts, setAlerts] = useState([]);

  const newModal = ({id, title, app}) => {
    const existingModal = modals.find(modal => modal.id === id);
    
    if (!existingModal) {      
      setModals(prevmodals => [...prevmodals, { id, title, app }]);
    } else {
      const alert_id = uuidv4();
      newAlert({
          'id': alert_id,
          'alert': <Alert key={alert_id} id={alert_id} title={<><FontAwesomeIcon icon={faTimesCircle} /> Error!</>} body={'Ya tienes esa ventana abierta.'} color={'danger'} removeAlert={removeAlert} timeout={3000} />
      });
    }
  };

  const removeModal = (id) => {
    setModals(prevModals => prevModals.filter(modal => modal.id !== id));
  };

  const newAlert = ({id, alert}) => {
    const existingAlert = alerts.find(alert => alert.id === id);
    if (!existingAlert) {
      setAlerts(prevAlerts => [...prevAlerts, { id, alert }]);
    }
  };

  const removeAlert = (id) => {
    setAlerts(prevAlerts => prevAlerts.filter(alert => alert.id !== id));
  };

  const commonProps = {
    newModal,
    removeModal,
    newAlert,
    removeAlert,
    Link,
    setAuth
  };
  
  const renderRoute = (path, Component) => (
    <Route path={path} element={<Component {...commonProps} />} />
  );  

  return (
    <Router>
      <div className='float-alerts'>
        {alerts.map(alert => alert.alert)}
      </div>
      <div className='auth'>
          <div className='info'>
            <div className='edge'>
              <svg viewBox='0 0 100 100'>
                <path d='M 0 0 C 100 20, 100 100, 100 100 L 100 100 L 100 0 Z' fill='white' />
              </svg>
            </div>
            <div className='container'>
              <div className='slogan'>
                <img src={logo2} alt='JVSoft' height={90} width={135} />
                <h1 className='title'>¡Bienvenidos!</h1>
                <h2 className='text'>El mejor software para tu restaurante</h2>
              </div>              
            </div>          
          </div>
          <div className='content'>
            <div className='edge'>
              <svg viewBox='0 0 100 100'>
                <path d='M 0 0 C 100 0, 100 100, 100 100 L 100 100 L 100 0 Z' />
              </svg>
            </div>
            <div className='container'>
              <Routes>
                {renderRoute('/auth/sign-in', SignIn)}
                {renderRoute('/auth/sign-up', SignUp)}
                <Route path='/*' element={<Navigate to='/auth/sign-in' />} />
              </Routes>              
            </div>
          </div>
      </div>
    </Router>
  );
}

export default AuthController;