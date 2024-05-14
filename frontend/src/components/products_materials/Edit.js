import React, { useEffect } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faFont, faSave } from '@fortawesome/free-solid-svg-icons';
import { applyInputEffects } from '../../assets/js/script';
import Select from '../Select';

const Edit = ({ data, btnSubmit, handleSubmit, handleInputChange }) => {
    useEffect(() => {
        applyInputEffects();      
    }, []);
    
    return (
        <form onSubmit={handleSubmit}>
            <div className='input-group input-warning'>                
                <div className='input'>
                    <label htmlFor='name'>Cantidad</label>
                    <FontAwesomeIcon icon={faFont} />
                    <input type='text' id='quantity' name='quantity' value={data.quantity || ''} onChange={handleInputChange} />
                </div>
                <div className='bar'></div>
            </div> 
            <Select name={'products_id'} endpoint={'/products'} data={data} color={'select-warning'} handleInputChange={handleInputChange} />
            <Select name={'raw_materials_id'} endpoint={'/raw/materials'} data={data} color={'select-warning'} handleInputChange={handleInputChange} />
            <button type='submit' className='btn btn-sm btn-warning mt-10px' disabled={btnSubmit}><FontAwesomeIcon icon={faSave} /> Guardar</button>
        </form>
    );
};

export default Edit;
