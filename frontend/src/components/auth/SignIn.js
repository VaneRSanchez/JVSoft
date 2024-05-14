import React, { useEffect, useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUser, faEyeSlash, faTimesCircle, faCheckCircle } from '@fortawesome/free-regular-svg-icons'
import { applyInputEffects } from '../../assets/js/script';
import { faRightFromBracket } from '@fortawesome/free-solid-svg-icons';
import { v4 as uuidv4 } from 'uuid';
import Alert from '../Alert';
import axios from 'axios';
import configData from '../../config.json';
import logo from '../../assets/images/logo-l.png';

const SignIn = ({  newModal, removeModal, newAlert, removeAlert, Link, setAuth }) => {
    const [data, setData] = useState({
        username: null,
        password: null
    });

    useEffect(() => {
        applyInputEffects();
    }, []);

    const handleSubmit = async (event) => {
        event.preventDefault();       

        try {
            let resp;
            resp = await axios.post(`${configData.api_url}/auth/sign-in`, data);
            const resp_data = resp.data;

            const alert_id = uuidv4();
            if(!resp_data.success){    
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
            localStorage.setItem('authToken', resp_data.token);   
            setAuth(true);      
        } catch (error) {
            const resp_data = error.response.data;
            
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
    }
    

    const handleInputChange = event => {
        const { name, value } = event.target;
        setData({ ...data, [name]: value });
    };

    return (
        <div className='view'>
            <div className='logo'>
                <img src={logo} alt='JVSoft' height={60} width={170} /> 
            </div> 
            <form onSubmit={handleSubmit}>
                <div className='input-group'>                
                    <div className='input'>
                        <label htmlFor='user'>Usuario</label>
                        <FontAwesomeIcon icon={faUser} />
                        <input type='text' id='username' name='username' value={data.username || ''} onChange={handleInputChange} />
                    </div>
                    <div className='bar'></div>
                </div>
                <div className='input-group'>                
                    <div className='input'>
                        <label htmlFor='password'>Contraseña</label>
                        <FontAwesomeIcon icon={faEyeSlash} />
                        <input type='password' id='password' name='password' value={data.password || ''} onChange={handleInputChange}/>
                    </div>
                    <div className='bar'></div>
                </div>
                <div className='remember-forgot'>
                    <div className='form-checkbox'>
                        <input className='checkbox' type='checkbox' id='remember' name='remember' />
                        <label htmlFor='remember'>Mantener la sesión</label>
                    </div>
                    <div className='a-forgot'>
                        <a href='https://google.com'>¿Has olvidado tu contraseña?</a>
                    </div>
                </div>
                <button className='btn btn-primary'><FontAwesomeIcon icon={faRightFromBracket} /> Iniciar sesion</button>
            </form>            
            <div className='info-auth'>
                <p>¿No tienes cuenta? <Link to="/auth/sign-up">REGISTRARSE</Link></p>
            </div>
        </div>
    );
};

export default SignIn;
