import React, { useEffect, useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faXmark } from '@fortawesome/free-solid-svg-icons';

const Alert = ({id, title, body, color, removeAlert, timeout }) => {
    const [isClosing, setIsClosing] = useState(false);
    
    const handleClose = () => {   
        setIsClosing(true);

        setTimeout(function(){
            removeAlert(id);
        }, 500);
    };

    useEffect(() => {
       if(timeout){
        setTimeout(function(){
            setIsClosing(true);

            setTimeout(function(){
                removeAlert(id);
            }, 500);
        }, timeout);
       }
    }, [timeout, id, removeAlert]);
      
    return(      
        <div className={`float-alert ${color} animate__animated animate__faster ${isClosing ? 'animate__fadeOut' : 'animate__fadeIn'}`}>
            <div className='header'>
            <h3 className='title'>{title}</h3>
                <div className='actions'>
                <div className='close' onClick={handleClose}><FontAwesomeIcon icon={faXmark} /></div>
                </div>
            </div>
            <div className='body'>
                {body}
            </div>
        </div>
    );
};

export default Alert;
