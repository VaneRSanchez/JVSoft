import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link, Navigate } from 'react-router-dom';
import { v4 as uuidv4 } from 'uuid';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faBacon, faBoxesStacked, faBurger, faCarrot, faCrosshairs, faDiagramProject, faList, faRocket, faRuler, faTicket, faTimesCircle, faUserLock, faWarehouse } from '@fortawesome/free-solid-svg-icons'
import logo from '../assets/images/logo3.png';
import Alert from '../components/Alert';
import InventoryRawMaterials from '../components/inventory_raw_materials/InventoryRawMaterials';
import MovementTypes from '../components/movement_types/MovementTypes';
import Products from '../components/products/Products';
import ProductCategories from '../components/product_categories/ProductCategories'
import ProductsMaterials from '../components/products_materials/ProductsMaterials'
import RawMaterials from '../components/raw_materials/RawMaterials';
import RawMaterialCategories from '../components/raw_material_categories/RawMaterialCategories'
import Units from '../components/units/Units';
import AppPos from '../components/pos/AppPos';
import PDFTicket from '../components/pdf/PDFTicket';
import AuthLogout from '../components/auth/AuthLogout';
import Sales from '../components/sales/Sales';

function AppController({ setAuth }) {
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

  const commonProps = {
    newModal,
    removeModal,
    newAlert,
    removeAlert,
    setAuth
  };
  
  const renderRoute = (path, Component) => (
    <Route path={path} element={<Component {...commonProps} />} />
  );

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
            <li className='separation'><span><FontAwesomeIcon icon={faRocket} /> App</span></li>
            <li><Link to="/app/pos"><FontAwesomeIcon icon={faCrosshairs} /> Punto de venta</Link></li>
            <li className='separation'><span><FontAwesomeIcon icon={faWarehouse} /> Inventarios</span></li>
            <li><Link to="/inventory/raw/materials"><FontAwesomeIcon icon={faBoxesStacked} /> Inventario materias primas</Link></li>
            <li className='separation mt-8px'><span><FontAwesomeIcon icon={faUserLock} /> Administracion</span></li>
            <li><Link to="/movement/types"><FontAwesomeIcon icon={faDiagramProject} /> Tipos de movimiento</Link></li>
            <li><Link to="/products"><FontAwesomeIcon icon={faBurger} /> Productos</Link></li>
            <li><Link to="/product/categories"><FontAwesomeIcon icon={faList} /> Categorías de producto</Link></li>
            <li><Link to="/products/materials"><FontAwesomeIcon icon={faBacon} /> Productos y materias</Link></li>
            <li><Link to="/raw/materials"><FontAwesomeIcon icon={faCarrot} /> Materias primas</Link></li>
            <li><Link to="/raw/material/categories"><FontAwesomeIcon icon={faList} /> Categorías de materias primas</Link></li>
            <li><Link to="/units"><FontAwesomeIcon icon={faRuler} /> Unidades</Link></li>
            <li><Link to="/sales"><FontAwesomeIcon icon={faTicket} /> Ventas</Link></li>

          </ul>
        </nav>
        <section className={menuActive ? 'content active' : 'content'}>
          <Routes>
            {renderRoute('/auth/logout', AuthLogout)}
            {renderRoute('/app/pos', AppPos)}
            {renderRoute('/inventory/raw/materials', InventoryRawMaterials)}
            {renderRoute('/movement/types', MovementTypes)}
            {renderRoute('/products', Products)}
            {renderRoute('/product/categories', ProductCategories)}
            {renderRoute('/products/materials', ProductsMaterials)}
            {renderRoute('/raw/materials', RawMaterials)}
            {renderRoute('/raw/material/categories', RawMaterialCategories)}
            {renderRoute('/units', Units)}
            {renderRoute('/sales', Sales)}
            {renderRoute('/pdf/sale', PDFTicket)}
            <Route path='/*' element={<Navigate to='/app/pos' />} />
          </Routes>
        </section>      
      </div>
    </Router>
  );
}

export default AppController;
