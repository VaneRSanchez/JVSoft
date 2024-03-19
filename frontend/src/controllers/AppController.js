import React, { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faAdd, faList, faUserLock } from '@fortawesome/free-solid-svg-icons'
import MyIcon from '../components/MyIcon';
import Modal from '../components/Modal';
import Add from '../components/product_categories/Add';
import Table from '../components/Table';

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
    <div className='app'>
      <nav className='navbar'>
        <div className='btn-menu'>
          <button className={menuActive ? 'btn active' : 'btn'} onClick={menuClick}>
            <MyIcon icon='menu' />
          </button>
        </div>
      </nav>
      {alerts.map(alert => alert.alert)}
      {modals.map(modal => modal.app)}
      <nav className={menuActive ? 'menu active' : 'menu'}>
        <ul>
          <li className='separation'><span><FontAwesomeIcon icon={faUserLock} /> Administracion</span></li>
          <li><a href='https://g.com'><FontAwesomeIcon icon={faList} /> Categorias de producto</a></li>
        </ul>
      </nav>
      <section className={menuActive ? 'content active' : 'content'}>
        <div className='info-bar'>
          <h3>Categorias de producto</h3>
          <ul>
            <li>Administracion</li>
            <li className='active'>/</li>
            <li className='active'>Categorias de producto</li>
          </ul>
        </div>        
        <div className='body g-8px'>
          <div className='grid-3 g-6px'>
            <div className='info-panel'>
              <div className='bar'></div>
              <div className='info'>
                <div className='icon'>
                  <FontAwesomeIcon icon={faList} />
                </div>
              </div>
              <div className='data'>
                <h2>0</h2>
                <span>Usuarios</span>
              </div>
            </div>
            <div className='info-panel dark'>
              <div className='bar'></div>
              <div className='info'>
                <div className='icon'>
                  <FontAwesomeIcon icon={faList} />
                </div>
              </div>
              <div className='data'>
                <h2>0</h2>
                <span>Usuarios</span>
              </div>
            </div>
            <div className='info-panel danger'>
            <div className='bar'></div>
              <div className='info'>
                <div className='icon'>
                  <FontAwesomeIcon icon={faList} />
                </div>
              </div>
              <div className='data'>
                <h2>0</h2>
                <span>Usuarios</span>
              </div>
              </div>
          </div>
          <div className='grid-t-4-1 g-6px'>
            <div className='panel'>
              <div className='header'>
                <h3 className='title'>Categorias</h3>
              </div>
              <div className='body'>
                <Table />
              </div>
            </div>
            <div className='panel'>
              <div className='header'>
                <h3 className='title'>Acciones</h3>
              </div>
              <div className='body pt-8px pb-8px'>
                <button 
                  className='btn btn-sm btn-primary' 
                  onClick={() => newModal({
                    'id': 'product-categories-add-modal',
                    'app': <Modal id={'product-categories-add-modal'} title={'Agregar categoria de producto'} body={<Add newAlert={newAlert} removeAlert={removeAlert} />} removeModal={removeModal} />
                  })}
                >
                  <FontAwesomeIcon icon={faAdd} /> Agregar
                </button>
              </div>
            </div>
          </div>
        </div>        
      </section>      
    </div>
  );
}

export default AppController;
