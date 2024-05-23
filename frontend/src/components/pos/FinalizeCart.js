import React, { useEffect, useState } from 'react';
import { useNavigate } from "react-router-dom";
import { v4 as uuidv4 } from 'uuid';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCheckCircle, faDollarSign, faTimesCircle } from '@fortawesome/free-solid-svg-icons';
import Alert from '../Alert';
import { applyInputEffects } from '../../assets/js/script';
import configData from '../../config.json';
import axios from 'axios';

const FinalizeCart = ({ cart, clearCart, newAlert, removeAlert, handleClose }) => {
    const [data, setData] = useState({
        payment: 0,
        cart: []
    });
    const [change, setChange] = useState(0);
    const [btnSubmit, setBtnSubmit] = useState(false);
    const navigate = useNavigate();

    useEffect(() => {
        applyInputEffects();
    }, []);

    useEffect(() => {
        setData({ ...data, cart: cart });

    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [cart]);

    useEffect(() => {
        const change = data.payment - calculateTotal();
        setChange(change);
        if(change < 0){
            setBtnSubmit(true);
        } else {
            setBtnSubmit(false);
        }        
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [cart, data]);

    const handleInputChange = event => {
        const { name, value } = event.target;
        setData({ ...data, [name]: value });
    };

    const calculateTotal = () => {
        let total = 0;
        cart.forEach(item => {
            total += item.price * item.quantity;
        });
        return total;
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        setBtnSubmit(true);

        try {
            const change = data.payment - calculateTotal();
            setChange(change);
            if(change < 0){
                setBtnSubmit(true);
                return false;
            }  

            const authToken = localStorage.getItem('authToken');
            const resp = await axios.post(`${configData.api_url}/sale/finalize`, data, 
            { 
                headers: {
                    'Authorization': `Bearer ${authToken}`
                }
            });
            const resp_data = resp.data;

            const alert_id = uuidv4();
            if(!resp_data.success){    
                setBtnSubmit(false);            
                newAlert({
                    'id': alert_id,
                    'alert': <Alert key={alert_id} id={alert_id} title={<><FontAwesomeIcon icon={faTimesCircle} /> Error!</>} body={resp_data.msg} color={'danger'} removeAlert={removeAlert} timeout={3000} />
                });
                return;
            }
            
            newAlert({
                'id': alert_id,
                'alert': <Alert key={alert_id} id={alert_id} title={<><FontAwesomeIcon icon={faCheckCircle} /> Exito!</>} body={resp_data.msg} color={'success'} removeAlert={removeAlert} timeout={3000} />
            });
            
            setTimeout(function(){
                navigate(`/pdf/sale?id=${resp_data.sale_id}`)
                handleClose();                
            }, 1000); 
            clearCart();
        } catch (error) {
            const resp_data = error.response.data;
            setBtnSubmit(false);
            
            if (typeof resp_data.msg === 'string') {
                const alert_id = uuidv4();
                newAlert({
                    'id': alert_id,
                    'alert': <Alert key={alert_id} id={alert_id} title={<><FontAwesomeIcon icon={faTimesCircle} /> Error!</>} body={resp_data.msg} color={'danger'} removeAlert={removeAlert} timeout={3000} />
                });
            } else if (typeof resp_data.msg === 'object') {
                Object.values(resp_data.msg).forEach(errorMsg => {
                    const alert_id = uuidv4();
                    newAlert({
                        'id': alert_id,
                        'alert': <Alert key={alert_id} id={alert_id} title={<><FontAwesomeIcon icon={faTimesCircle} /> Error!</>} body={errorMsg} color={'danger'} removeAlert={removeAlert} timeout={3000} />
                    });
                });
            }
        }       
    };

    return (
        <form onSubmit={handleSubmit}>
            <div className='input-group'>
                <div className='input'>
                    <label htmlFor='payment'>Con cuanto pago?</label>
                    <FontAwesomeIcon icon={faDollarSign} />
                    <input type='number' id='payment' name='payment' value={data.payment}  onChange={handleInputChange}   />
                </div>
                <div className='bar'></div>
            </div>
            <div className='row justify-content-end align-items-center g-8px mt-10px'>
                <h3>Cambio:</h3>
                <h2>${ change }</h2>
            </div>
            <button type='submit' className='btn btn-sm btn-primary mt-10px' disabled={btnSubmit}><FontAwesomeIcon icon={faCheckCircle} /> Finalizar</button>
        </form>
    );
};

export default FinalizeCart;
