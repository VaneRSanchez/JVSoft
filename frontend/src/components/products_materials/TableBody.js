import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faBurger, faEdit, faFingerprint } from '@fortawesome/free-solid-svg-icons'
import Modal from '../Modal';
import SendData from '../SendData';
import Edit from './Edit';

const TableBody = ({ data, setBtnEdit, newModal, removeModal, newAlert, removeAlert, reloadTable }) => {
    const handleEdit = (entry) => {
        newModal({
            'id': `products-materials-edit-${entry.id}-modal`,
            'app':  
                <Modal 
                    key={`products-materials-edit-${entry.id}-modal`} 
                    id={`products-materials-edit-${entry.id}-modal`} 
                    color={'warning'}
                    title={'Editar producto y su materia'} 
                    body={
                        <SendData
                            endpoint={'/products/materials'}
                            type={'PUT'}
                            data={{
                                'id': entry.id,
                                'quantity': entry.quantity,
                                'products_id': entry.products.id,
                                'raw_materials_id': entry.raw_materials.id
                            }}
                            body={<Edit />}
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
                className='btn btn-sm btn-warning'
                disabled
            >
                <FontAwesomeIcon icon={faEdit} /> Editar
            </button>
        );
    };  

    const handleClick = (entry) => {
        setBtnEdit(
            <button 
                className='btn btn-sm btn-warning' 
                onClick={() => handleEdit(entry)}
            >
                <FontAwesomeIcon icon={faEdit} /> Editar
            </button>
        );
    };   

    return (
        <tbody>
            {data.map((entry, index) => (
                <tr 
                    key={index}
                    onClick={() => handleClick(entry)}
                >
                    <td><span className='badge'><FontAwesomeIcon icon={faFingerprint} /> {entry.id}</span></td>
                    <td>{entry.quantity} ({entry.raw_materials.units.name})</td>
                    <td><span className='badge'><FontAwesomeIcon icon={faBurger} /> {entry.products.name}</span></td>
                    <td>{entry.raw_materials.name}</td>
                </tr>
            ))}
        </tbody>
    );
};

export default TableBody;
