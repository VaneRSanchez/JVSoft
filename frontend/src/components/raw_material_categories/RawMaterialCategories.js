import React, { useEffect, useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faAdd, faEdit, faEye, faEyeSlash, faList } from '@fortawesome/free-solid-svg-icons'
import Modal from '../Modal';
import Add from './Add';
import Table from '../Table';
import TableBody from './TableBody';
import { Requests } from '../../assets/js/Requests';

const RawMaterialCategories = ({ newModal, removeModal, newAlert, removeAlert }) => {
    const [forceTableUpdate, setForceTableUpdate] = useState(false);
    const [btnEdit, setBtnEdit] = useState(
        <button 
            className='btn btn-sm btn-warning'
            disabled
        >
            <FontAwesomeIcon icon={faEdit} /> Editar
        </button>
    );
    const [dataStatistics, setDataStatistics] = useState({
        count_total: 0,
        count_active: 0,
        count_hidden: 0
    });

    const columnsTable = {
        'id': 'ID',
        'name': 'Nombre',
        'status': 'Estatus'
    };
      
    const reloadTable = () => {
        setForceTableUpdate(prevState => !prevState);
    };   

    useEffect(() => {
        const setStatistics = async () => {
            const response = await Requests({ endpoint: '/raw/material/categories', method: 'GET', data: {query: 'statistics'} });
            if (response.data) {
                setDataStatistics({
                    count_total: response.data.count_total,
                    count_active: response.data.count_active,
                    count_hidden: response.data.count_hidden
                });
            }
        };

        setStatistics();
    }, [forceTableUpdate]);

    return (
        <div>
            <div className='info-bar'>
                <h3>Categorías de materias primas</h3>
                <ul>
                    <li>Administracion</li>
                    <li className='active'>/</li>
                    <li className='active'>Categorías de materias primas</li>
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
                            <h2>{dataStatistics.count_total}</h2>
                            <span>Total</span>
                        </div>
                    </div>
                    <div className='info-panel dark'>
                        <div className='bar'></div>
                        <div className='info'>
                            <div className='icon'>
                                <FontAwesomeIcon icon={faEye} />
                            </div>
                        </div>
                        <div className='data'>
                            <h2>{dataStatistics.count_active}</h2>
                            <span>Activo</span>
                        </div>
                    </div>
                    <div className='info-panel danger'>
                        <div className='bar'></div>
                        <div className='info'>
                            <div className='icon'>
                                <FontAwesomeIcon icon={faEyeSlash} />
                            </div>
                        </div>
                        <div className='data'>
                            <h2>{dataStatistics.count_hidden}</h2>
                            <span>Oculto</span>
                        </div>
                    </div>
                </div>
                <div className='grid-t-4-1 g-6px'>
                    <div className='panel'>
                        <div className='header'>
                            <h3 className='title'>Categorías</h3>
                        </div>
                        <div className='body'>
                            <Table 
                                key={forceTableUpdate} 
                                endpoint={'/raw/material/categories'} 
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
                                    'id': 'raw-material-categories-add-modal',
                                    'app': <Modal key={'raw-material-categories-add-modal'} id={'raw-material-categories-add-modal'} color={'primary'} title={'Agregar categoría de materia prima'} body={<Add newAlert={newAlert} removeAlert={removeAlert} reloadTable={reloadTable} />} removeModal={removeModal} />
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

export default RawMaterialCategories;