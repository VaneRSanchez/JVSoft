import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faDollarSign, faFingerprint } from '@fortawesome/free-solid-svg-icons'
import Modal from '../Modal';
import AddCart from './AddCart';

const TableBody = ({ data, addToCart, newModal, removeModal, newAlert, removeAlert }) => {
    const handleClick = (item) => {
        newModal({
            'id': `app-cart-add-${item.id}-modal`,
            'app':
                <Modal
                    key={`app-cart-add-${item.id}-modal`}
                    id={`app-cart-add-${item.id}-modal`}
                    color={'primary'}
                    title={'Agregar al carrito'}
                    body={
                        <AddCart item={item} addToCart={addToCart} newAlert={newAlert} removeAlert={removeAlert}/>
                    }
                    removeModal={removeModal}
                />
        });
    };

    return (
        <tbody>
            {data.map((item, index) => (
                <tr
                    key={index}
                    onClick={() => handleClick(item)}                >
                    <td><span className='badge'><FontAwesomeIcon icon={faFingerprint} /> {item.id}</span></td>
                    <td>{item.name}</td>
                    <td>{item.description}</td>
                    <td><span className='badge'><FontAwesomeIcon icon={faDollarSign} /> {item.price}</span></td>
                    <td>{item.product_categories.name}</td>
                </tr>
            ))}
        </tbody>
    );
};

export default TableBody;
