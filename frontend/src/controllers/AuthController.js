import React, { useEffect } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUser, faEyeSlash } from '@fortawesome/free-regular-svg-icons'
import { applyInputEffects } from '../assets/js/script';
import { faRightFromBracket } from '@fortawesome/free-solid-svg-icons';
import logo from '../assets/images/logo-l.png';
import logo2 from '../assets/images/logo4.png';

function AuthController() {
  useEffect(() => {
    applyInputEffects();
  }, []);
  
  return (
    <div className='auth'>
        <div className='info'>
          <div className='edge'>
            <svg viewBox='0 0 100 100'>
              <path d='M 0 0 C 100 20, 100 100, 100 100 L 100 100 L 100 0 Z' fill='white' />
            </svg>
          </div>
          <div className='container'>
            <div className='slogan'>
              <img src={logo2} alt='JVSoft' height={90} width={135} />
              <h1 className='title'>¡Bienvenidos!</h1>
              <h2 className='text'>El mejor software para tu restaurante</h2>
            </div>              
          </div>          
        </div>
        <div className='content'>
          <div className='edge'>
            <svg viewBox='0 0 100 100'>
              <path d='M 0 0 C 100 0, 100 100, 100 100 L 100 100 L 100 0 Z' />
            </svg>
          </div>
          <div className='container'>
            <div className='view'>
              <div className='logo'>
                <img src={logo} alt='JVSoft' height={60} width={170} /> 
              </div> 
              <div className='input-group'>                
                <div className='input'>
                  <label htmlFor='user'>Usuario</label>
                  <FontAwesomeIcon icon={faUser} />
                  <input type='text' id='user' name='user' />
                </div>
                <div className='bar'></div>
              </div>
              <div className='input-group'>                
                <div className='input'>
                  <label htmlFor='password'>Contraseña</label>
                  <FontAwesomeIcon icon={faEyeSlash} />
                  <input type='password' id='password' name='password' />
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
              <div className='info-auth'>
                <p>¿No tienes cuenta? <a href='https://google.com'>REGISTRARSE</a></p>
              </div>
            </div>
          </div>
        </div>
    </div>
  );
}

export default AuthController;