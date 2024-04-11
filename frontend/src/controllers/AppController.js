import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { v4 as uuidv4 } from 'uuid';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faBurger, faCarrot, faDiagramProject, faList, faRuler, faTimesCircle, faUserLock } from '@fortawesome/free-solid-svg-icons'
import ProductCategories from '../components/product_categories/ProductCategories'
import RawMaterialCategories from '../components/raw_material_categories/RawMaterialCategories'
import logo from '../assets/images/logo3.png';
import Alert from '../components/Alert';
import Units from '../components/units/Units';
import MovementTypes from '../components/movement_types/MovementTypes';
import Products from '../components/products/Products';

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
            <li><Link to="/movement/types"><FontAwesomeIcon icon={faDiagramProject} /> Tipos de movimiento</Link></li>
            <li><Link to="/products"><FontAwesomeIcon icon={faBurger} /> Productos</Link></li>
            <li><Link to="/product/categories"><FontAwesomeIcon icon={faList} /> Categorías de producto</Link></li>
            <li><Link to="/raw/material/categories"><FontAwesomeIcon icon={faCarrot} /> Categorías de materias primas</Link></li>
            <li><Link to="/units"><FontAwesomeIcon icon={faRuler} /> Unidades</Link></li>
          </ul>
        </nav>
        <section className={menuActive ? 'content active' : 'content'}>
          <Routes>
            <Route path="/movement/types" element={<MovementTypes newModal={newModal} removeModal={removeModal} newAlert={newAlert} removeAlert={removeAlert} />} />
            <Route path="/products" element={<Products newModal={newModal} removeModal={removeModal} newAlert={newAlert} removeAlert={removeAlert} />} />
            <Route path="/product/categories" element={<ProductCategories newModal={newModal} removeModal={removeModal} newAlert={newAlert} removeAlert={removeAlert} />} />
            <Route path="/raw/material/categories" element={<RawMaterialCategories newModal={newModal} removeModal={removeModal} newAlert={newAlert} removeAlert={removeAlert} />} />
            <Route path="/units" element={<Units newModal={newModal} removeModal={removeModal} newAlert={newAlert} removeAlert={removeAlert} />} />
          </Routes>
        </section>      
      </div>
    </Router>
  );
}

export default AppController;
