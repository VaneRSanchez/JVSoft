import React, { useState } from 'react';
import Draggable from 'react-draggable';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faXmark } from '@fortawesome/free-solid-svg-icons';

const Modal = ({id, title, body, removeModal}) => {
    const [position, setPosition] = useState({ x: window.innerWidth / 2 - 200, y: 0 });
    const [isClosing, setIsClosing] = useState(false);

    const handleDrag = (e, ui) => {
        const { x, y } = ui;
        setPosition({ x, y });
    };

    const handleClose = () => {   
        setIsClosing(true);

        setTimeout(function(){
            removeModal(id);
        }, 500);
    };
      
    return(
        <Draggable            
            handle='.header'
            bounds='parent'
            position={position}
            onDrag={handleDrag}
        >        
            <div className={`window animate__animated animate__faster ${isClosing ? 'animate__fadeOut' : 'animate__fadeIn'}`}>
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
        </Draggable>
    );
};

export default Modal;
