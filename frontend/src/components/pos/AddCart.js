import React, { useEffect, useState } from 'react';
import { v4 as uuidv4 } from 'uuid';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faAdd, faCheckCircle, faFont } from '@fortawesome/free-solid-svg-icons';
import Alert from '../Alert';
import { applyInputEffects } from '../../assets/js/script';

const AddCart = ({ item, addToCart, newAlert, removeAlert, handleClose }) => {
    const [data, setData] = useState({
        name: item.name,
        quantity: 1,
    });
    const [btnSubmit, setBtnSubmit] = useState(false);

    useEffect(() => {
        applyInputEffects();
    }, []);

    const handleInputChange = event => {
        const { name, value } = event.target;
        setData({ ...data, [name]: value });
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        setBtnSubmit(true);
        const product = {
            id: item.id,
            name: item.name,
            price: item.price,
            product_categories: {
                id: item.product_categories.id,
                name: item.product_categories.name
            },
            quantity: data.quantity
        };

        const alert_id = uuidv4();
        newAlert({
            'id': alert_id,
            'alert': <Alert key={alert_id} id={alert_id} title={<><FontAwesomeIcon icon={faCheckCircle} /> Exito!</>} body={'Se agrego correctamente.'} color={'success'} removeAlert={removeAlert} timeout={3000} />
        });
        
        setTimeout(function(){
            handleClose();                
        }, 1000); 
        addToCart(product);
    };

    return (
        <form onSubmit={handleSubmit}>
            <div className='input-group'>
                <div className='input'>
                    <label htmlFor='name'>Nombre</label>
                    <FontAwesomeIcon icon={faFont} />
                    <input type='text' id='name' name='name' value={data.name || ''} disabled />
                </div>
                <div className='bar'></div>
            </div>
            <div className='input-group mt-6px'>
                <div className='input'>
                    <label htmlFor='quantity'>Cantidad</label>
                    <FontAwesomeIcon icon={faFont} />
                    <input type='number' id='quantity' name='quantity' value={data.quantity} onChange={handleInputChange} />
                </div>
                <div className='bar'></div>
            </div>
            <button type='submit' className='btn btn-sm btn-primary mt-10px' disabled={btnSubmit}><FontAwesomeIcon icon={faAdd} /> Agregar</button>
        </form>
    );
};

export default AddCart;
