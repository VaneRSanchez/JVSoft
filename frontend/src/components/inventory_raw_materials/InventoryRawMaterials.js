import React, { useEffect, useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faAdd, faChartLine, faInfoCircle, faTimes, faTriangleExclamation } from '@fortawesome/free-solid-svg-icons'
import Modal from '../Modal';
import Add from './Add';
import Table from '../Table';
import TableBody from './TableBody';
import TableBodyFind from './TableBodyFind';
import { Requests } from '../../assets/js/Requests';

const InventoryRawMaterials = ({ newModal, removeModal, newAlert, removeAlert }) => {
    const [forceTableUpdate, setForceTableUpdate] = useState(false);
    const [btnEdit, setBtnEdit] = useState(
        <button
            className='btn btn-sm btn-danger'
            disabled
        >
            <FontAwesomeIcon icon={faTimes} /> Cancelar
        </button>
    );

    const [dataStatistics, setDataStatistics] = useState({
        count_movements: 0,
        count_raw_materials_expiration: 0,
        count_raw_materials_expired: 0,
    });

    const columnsTable = {
        'id': 'ID',
        'raw_materials.name': 'Materia prima',
        'quantity': 'Cantidad',
        'date_exp': 'Fecha de expiracion',
        'movement_types.name': 'Tipo de movimiento',
        'date_reg': 'Fecha de registro',
        'status': 'Estatus',
    };

    const columnsTableFind = {
        'id': 'ID',
        'name': 'Materia prima',
        'raw_material_categories.name': 'Categoria',
        'total_quantity': 'Cantidad en el inventario',
    };

    const reloadTable = () => {
        setForceTableUpdate(prevState => !prevState);
    };

    useEffect(() => {
        const setStatistics = async () => {
            const response = await Requests({ endpoint: '/inventory/raw/materials', method: 'GET', data: {query: 'statistics'} });
            if (response.data) {
                setDataStatistics({
                    count_movements: response.data.count_movements,
                    count_raw_materials_expiration: response.data.count_raw_materials_expiration,
                    count_raw_materials_expired: response.data.count_raw_materials_expired,
                });
            }
        };

        setStatistics();
    }, [forceTableUpdate]);

    return (
        <div>
            <div className='info-bar'>
                <h3>Inventario - Materias Primas</h3>
                <ul>
                    <li>Inventarios</li>
                    <li className='active'>/</li>
                    <li className='active'>Materias primas</li>
                </ul>
            </div>
            <div className='body g-8px'>
                <div className='grid-3 g-6px'>
                    <div className='info-panel'>
                        <div className='bar'></div>
                        <div className='info'>
                            <div className='icon'>
                                <FontAwesomeIcon icon={faChartLine} />
                            </div>
                        </div>
                        <div className='data'>
                            <h2>{dataStatistics.count_movements}</h2>
                            <span>Movimientos realizados</span>
                        </div>
                    </div>
                    <div className='info-panel dark'>
                        <div className='bar'></div>
                        <div className='info'>
                            <div className='icon'>
                                <FontAwesomeIcon icon={faInfoCircle} />
                            </div>
                        </div>
                        <div className='data'>
                            <h2>{dataStatistics.count_raw_materials_expiration}</h2>
                            <span>Por caducar</span>
                        </div>
                    </div>
                    <div className='info-panel danger'>
                        <div className='bar'></div>
                        <div className='info'>
                            <div className='icon'>
                                <FontAwesomeIcon icon={faTriangleExclamation} />
                            </div>
                        </div>
                        <div className='data'>
                            <h2>{dataStatistics.count_raw_materials_expired}</h2>
                            <span>Ya caducados</span>
                        </div>
                    </div>
                </div>
                <div className='grid-t-1 g-6px'>
                    <div className='panel'>
                        <div className='header'>
                            <h3 className='title'>Materias primas</h3>
                        </div>
                        <div className='body'>
                            <Table
                                key={forceTableUpdate}
                                endpoint={'/inventory/raw/materials'}
                                columns={columnsTableFind}
                                tbody={
                                    <TableBodyFind
                                        setBtnEdit={setBtnEdit}
                                        newModal={newModal}
                                        removeModal={removeModal}
                                        newAlert={newAlert}
                                        removeAlert={removeAlert}
                                        reloadTable={reloadTable}
                                    />
                                }
                                query_name='table_raw_materials'
                            />
                        </div>
                    </div>
                </div>
                <div className='grid-t-4-1 g-6px'>
                    <div className='panel'>
                        <div className='header'>
                            <h3 className='title'>Movimientos</h3>
                        </div>
                        <div className='body'>
                            <Table
                                key={forceTableUpdate}
                                endpoint={'/inventory/raw/materials'}
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
                                    'id': 'inventory-raw-materials-add-modal',
                                    'app': <Modal key={'inventory-raw-materials-add-modal'} id={'inventory-raw-materials-add-modal'} color={'primary'} title={'Agregar inventario de la materia prima'} body={<Add newAlert={newAlert} removeAlert={removeAlert} reloadTable={reloadTable} />} removeModal={removeModal} />
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

export default InventoryRawMaterials;