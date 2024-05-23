import React, { useRef, useState } from 'react';
import Draggable from 'react-draggable';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faXmark } from '@fortawesome/free-solid-svg-icons';

const Modal = ({id, color, title, body, removeModal}) => {
    const [position, setPosition] = useState({ x: window.innerWidth / 2 - 180, y: -55 });
    const [isClosing, setIsClosing] = useState(false);
    const modalRef = useRef(null);

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
            handle='.title'
            bounds='parent'
            position={position}
            onDrag={handleDrag}
            nodeRef={modalRef}
        >        
            <div className={`window window-${color} animate__animated animate__faster ${isClosing ? 'animate__fadeOut' : 'animate__fadeIn'}`} ref={modalRef}>
                <div className='header'>
                    <h3 className='title'>{title}</h3>
                    <div className='actions'>
                        <div className='close' onClick={handleClose}><FontAwesomeIcon icon={faXmark} /></div>
                    </div>
                </div>
                <div className='body'>
                    {React.cloneElement(body, { handleClose: handleClose })} 
                </div>
            </div>
        </Draggable>
    );
};

export default Modal;
