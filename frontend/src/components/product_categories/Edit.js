import React, { useEffect } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faAdd, faFont } from '@fortawesome/free-solid-svg-icons';
import { applyInputEffects } from '../../assets/js/script';

const Edit = ({ myData, btnSubmit, handleSubmit, handleInputChange }) => {
    useEffect(() => {
        applyInputEffects();      
    }, []);
    
    return (
        <form onSubmit={handleSubmit}>
            <div className='input-group input-warning'>                
                <div className='input'>
                    <label htmlFor='name'>Nombre</label>
                    <FontAwesomeIcon icon={faFont} />
                    <input type='text' id='name' name='name' value={myData.name || ''} onChange={handleInputChange} />
                </div>
                <div className='bar'></div>
            </div>
            <button type='submit' className='btn btn-sm btn-warning mt-10px' disabled={btnSubmit}><FontAwesomeIcon icon={faAdd} /> Agregar</button>
        </form>
    );
};

export default Edit;
