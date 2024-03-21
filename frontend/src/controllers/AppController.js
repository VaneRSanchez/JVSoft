import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { v4 as uuidv4 } from 'uuid';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faList, faTimesCircle, faUserLock } from '@fortawesome/free-solid-svg-icons'
import ProductCategories from '../components/product_categories/ProductCategories'
import logo from '../assets/images/logo3.png';
import Alert from '../components/Alert';

function AppController() {
  const [menuActive, setMenuActive] = useState(false);
  const [modals, setModals] = useState([]);
  const [alerts, setAlerts] = useState([]);

  const menuClick = () => {
    setMenuActive(!menuActive);
  }

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

  return (
    <Router>
      <div className='app'>
        <nav className='navbar'>
          <div className='btn-menu'>
            <button className={menuActive ? 'btn active' : 'btn'} onClick={menuClick}>
            <img src={logo} alt='JVSoft' height={42} width={130} />         
            </button>
          </div>
         
        </nav>
        <div className='float-alerts'>
          {alerts.map(alert => alert.alert)}
        </div>
        {modals.map(modal => modal.app)}
        <nav className={menuActive ? 'menu active' : 'menu'}>
          <ul>
            <li className='separation'><span><FontAwesomeIcon icon={faUserLock} /> Administracion</span></li>
            <li><Link to="/product/categories"><FontAwesomeIcon icon={faList} /> Categorias de producto</Link></li>
          </ul>
        </nav>
        <section className={menuActive ? 'content active' : 'content'}>
          <Routes>
            <Route path="/product/categories" element={<ProductCategories newModal={newModal} removeModal={removeModal} newAlert={newAlert} removeAlert={removeAlert} />} />
          </Routes>
        </section>      
      </div>
    </Router>
  );
}

export default AppController;
