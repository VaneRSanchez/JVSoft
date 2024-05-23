import React, { useEffect, useState } from 'react';
import { v4 as uuidv4 } from 'uuid';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCheckCircle, faTimesCircle } from '@fortawesome/free-solid-svg-icons';
import axios from 'axios';
import Alert from './Alert';
import { applyInputEffects } from '../assets/js/script';
import configData from '../config.json';

const SendData = ({ endpoint, type, data, body, newAlert, removeAlert, handleClose, reloadTable }) => {
    const [myData, setMyData] = useState(data);
    const [btnSubmit, setBtnSubmit] = useState(false);

    useEffect(() => {
        applyInputEffects();      
    }, []);

    const handleInputChange = event => {
        const { name, value } = event.target;
        setMyData({ ...myData, [name]: value });
    };

    const handleSubmit = async (event) => {
        const authToken = localStorage.getItem('authToken');
        event.preventDefault();
        
        setBtnSubmit(true);

        try {
            let resp;

            if(type === 'POST'){
                resp = await axios.post(`${configData.api_url}${endpoint}`, myData, { 
                    headers: {
                        'Authorization': `Bearer ${authToken}`
                    }
                });
            } else if(type === 'PUT'){
                resp = await axios.put(`${configData.api_url}${endpoint}`, myData, { 
                    headers: {
                        'Authorization': `Bearer ${authToken}`
                    }
                });
            } else if(type === 'DELETE'){
                resp = await axios.delete(`${configData.api_url}${endpoint}`, {
                    data: myData,
                    headers: {
                        'Authorization': `Bearer ${authToken}`
                    }
                });
            }

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

    return React.cloneElement(body, { data: myData, btnSubmit: btnSubmit, handleSubmit: handleSubmit, handleInputChange: handleInputChange });
};

export default SendData;