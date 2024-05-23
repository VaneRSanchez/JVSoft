import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faBasketShopping, faFingerprint, faTimes } from '@fortawesome/free-solid-svg-icons'
import Modal from '../Modal';
import SendData from '../SendData';
import Cancel from './Cancel';

const TableBodyFind = ({ data, setBtnEdit, newModal, removeModal, newAlert, removeAlert, reloadTable }) => {
    const handleEdit = (entry) => {
        newModal({
            'id': `inventory-raw-materials-edit-${entry.id}-modal`,
            'app':  
                <Modal 
                    key={`inventory-raw-materials-edit-${entry.id}-modal`} 
                    id={`inventory-raw-materials-edit-${entry.id}-modal`} 
                    color={'danger'}
                    title={'Cancelar inventario de la materia prima'} 
                    body={
                        <SendData
                            endpoint={'/inventory/raw/materials'}
                            type={'DELETE'}
                            data={{
                                'id': entry.id
                            }}
                            body={<Cancel />}
                            newAlert={newAlert} 
                            removeAlert={removeAlert} 
                            reloadTable={reloadTable} 
                        />
                    } 
                    removeModal={removeModal} 
                />
        });

        setBtnEdit( 
            <button 
                className='btn btn-sm btn-danger'
                disabled
            >
                <FontAwesomeIcon icon={faTimes} /> Cancelar
            </button>
        );
    };  

    const handleClick = (entry) => {
        if(entry.status){
            setBtnEdit(
                <button 
                    className='btn btn-sm btn-danger' 
                    onClick={() => handleEdit(entry)}
                >
                    <FontAwesomeIcon icon={faTimes} /> Cancelar
                </button>
            );
        } else {
            setBtnEdit(
                <button 
                    className='btn btn-sm btn-danger' 
                    disabled={true}
                >
                    <FontAwesomeIcon icon={faTimes} /> Cancelar
                </button>
            );
        }      
    };   

    return (
        <tbody>
            {data.map((entry, index) => (
                <tr 
                    key={index}
                    onClick={() => handleClick(entry)}
                >
                    <td><span className='badge'><FontAwesomeIcon icon={faFingerprint} /> {entry.id}</span></td>
                    <td>{entry.name}</td>
                    <td>{entry.raw_material_categories.name}</td>
                    <td><span className='badge'><FontAwesomeIcon icon={faBasketShopping} /> {entry.total_quantity}</span></td>
                </tr>
            ))}
        </tbody>
    );
};

export default TableBodyFind;
