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
          <div className="container">
            hola
          </div>
        </div>
        <div className="content">
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