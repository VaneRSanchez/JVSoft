import React, { useEffect, useState } from 'react';
import { v4 as uuidv4 } from 'uuid';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faAdd, faCheckCircle, faFont, faTimesCircle } from '@fortawesome/free-solid-svg-icons';
import axios from 'axios';
import Alert from '../Alert';
import { applyInputEffects } from '../../assets/js/script';
import configData from '../../config.json';

const Add = ({ newAlert, removeAlert, handleClose, reloadTable }) => {
    const [tableData, setTableData] = useState({
        name: null,
    });
    const [btnSubmit, setBtnSubmit] = useState(false);

    useEffect(() => {
        applyInputEffects();
    }, []);

    const handleInputChange = event => {
        const { name, value } = event.target;
        setTableData({ ...tableData, [name]: value });
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        
        setBtnSubmit(true);

        try {
            const authToken = localStorage.getItem('authToken');
            const resp = await axios.post(`${configData.api_url}/product/categories`, tableData,
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
                reloadTable();
                handleClose();                
            }, 1000);           
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
                    <label htmlFor='name'>Nombre</label>
                    <FontAwesomeIcon icon={faFont} />
                    <input type='text' id='name' name='name' value={tableData.name || ''} onChange={handleInputChange} />
                </div>
                <div className='bar'></div>
            </div>
            <button type='submit' className='btn btn-sm btn-primary mt-10px' disabled={btnSubmit}><FontAwesomeIcon icon={faAdd} /> Agregar</button>
        </form>
    );
};

export default Add;
