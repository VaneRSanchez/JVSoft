import React, { useEffect } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
//import { faLock } from '@fortawesome/free-solid-svg-icons'
import { faUser, faEyeSlash } from '@fortawesome/free-regular-svg-icons'

import { applyInputEffects } from '../assets/js/script';

function AuthController() {
  useEffect(() => {
    applyInputEffects();
  }, []);
  
  return (
    <div className="auth">
        <div className="info">
          <div className="edge">
            <svg viewBox="0 0 100 100">
              <path d="M 0 0 C 100 20, 100 100, 100 100 L 100 100 L 100 0 Z" fill="white" />
            </svg>
          </div>
          <div className="container">
            <div className="slogan">
              <h1 className="title">JVSoft</h1>
              <h2 className="text">¡El mejor software para tu restaurante!</h2>
            </div>              
          </div>          
        </div>
        <div className="content">
          <div className="edge">
            <svg viewBox="0 0 100 100">
              <path d="M 0 0 C 100 0, 100 100, 100 100 L 100 100 L 100 0 Z" />
            </svg>
          </div>
          <div className="container">
            <div className="view">
              <div className="input-group">                
                <div className="input">
                  <label htmlFor="user">Usuario</label>
                  <FontAwesomeIcon icon={faUser} />
                  <input type="text" id="user" name="user" />
                </div>
                <div className="bar"></div>
              </div>
              <div className="input-group">                
                <div className="input">
                  <label htmlFor="password">Contraseña</label>
                  <FontAwesomeIcon icon={faEyeSlash} />
                  <input type="password" id="password" name="password" />
                </div>
                <div className="bar"></div>
              </div>
              <div className="remember-forgot">
                <div className="form-checkbox">
                  <input className="checkbox" type="checkbox" id="remember" name="remember" />
                  <label htmlFor="remember">Mantener la sesión</label>
                </div>
                <div className="a-forgot">
                  <a href="https://google.com">¿Has olvidado tu contraseña?</a>
                </div>
              </div>
              <button className="btn btn-primary">Iniciar sesion</button>
              <div className="info-auth">
                <p>¿No tienes cuenta? <a href="https://google.com">REGISTRARSE</a></p>
              </div>
            </div>
          </div>
        </div>
    </div>
  );
}

export default AuthController;