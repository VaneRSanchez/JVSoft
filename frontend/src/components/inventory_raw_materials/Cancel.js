import React, { useEffect } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faWarning } from '@fortawesome/free-solid-svg-icons';
import { applyInputEffects } from '../../assets/js/script';

const Cancel = ({ data, btnSubmit, handleSubmit, handleInputChange }) => {
    useEffect(() => {
        applyInputEffects();      
    }, []);
    
    return (
        <form onSubmit={handleSubmit}>
            <h3>Estas seguro/a de que deseas cancelar?</h3>
            <button type='submit' className='btn btn-sm btn-danger mt-5px' disabled={btnSubmit}><FontAwesomeIcon icon={faWarning} /> Cancelar</button>
        </form>
    );
};

export default Cancel;
