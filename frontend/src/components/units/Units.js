import React, { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faAdd, faEdit, faList } from '@fortawesome/free-solid-svg-icons'
import Modal from '../Modal';
import Add from './Add';
import Table from '../Table';
import TableBody from './TableBody';

const Units = ({ newModal, removeModal, newAlert, removeAlert }) => {
    const [forceTableUpdate, setForceTableUpdate] = useState(false);
    const [btnEdit, setBtnEdit] = useState(
        <button 
            className='btn btn-sm btn-warning'
            disabled
        >
            <FontAwesomeIcon icon={faEdit} /> Editar
        </button>
    );

    const columnsTable = {
        'id': 'ID',
        'name': 'Nombre',
    };
      
    const reloadTable = () => {
        setForceTableUpdate(prevState => !prevState);
    };   

    return (
        <div>
            <div className='info-bar'>
                <h3>Unidades</h3>
                <ul>
                    <li>Administracion</li>
                    <li className='active'>/</li>
                    <li className='active'>Unidades</li>
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
                            <h3 className='title'>Unidades</h3>
                        </div>
                        <div className='body'>
                            <Table 
                                key={forceTableUpdate} 
                                endpoint={'/units'} 
                                columns={columnsTable} 
                                tbody={
                                    <TableBody 
                                        setBtnEdit={setBtnEdit}
                                        newModal={newModal} 
                                        removeModal={removeModal} 
                                        newAlert={newAlert} 
                                        removeAlert={removeAlert} 
                                        reloadTable={reloadTable}
                                    />
                                } 
                            />
                        </div>
                    </div>
                    <div className='panel'>
                        <div className='header'>
                            <h3 className='title'>Acciones</h3>
                        </div>
                        <div className='body row pt-8px pb-8px g-4px'>
                            <button 
                                className='btn btn-sm btn-primary' 
                                onClick={() => newModal({
                                    'id': 'units-add-modal',
                                    'app': <Modal key={'units-add-modal'} id={'units-add-modal'} color={'primary'} title={'Agregar unidad'} body={<Add newAlert={newAlert} removeAlert={removeAlert} reloadTable={reloadTable} />} removeModal={removeModal} />
                                })}
                            >
                                <FontAwesomeIcon icon={faAdd} /> Agregar
                            </button>
                            {btnEdit}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Units;