import React, { useEffect, useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faFont, faSave } from '@fortawesome/free-solid-svg-icons';
import { applyInputEffects } from '../../assets/js/script';

const Edit = ({ data, btnSubmit, handleSubmit, handleInputChange }) => {
    const [isChecked, setIsChecked] = useState(data.status);

    const handleToggle = () => {
        const newStatus = !isChecked;
        setIsChecked(newStatus);
        handleInputChange({ target: { name: 'status', value: newStatus } })
    };

    useEffect(() => {
        applyInputEffects();      
    }, []);
    
    return (
        <form onSubmit={handleSubmit}>
            <div className='input-group input-warning'>                
                <div className='input'>
                    <label htmlFor='name'>Nombre</label>
                    <FontAwesomeIcon icon={faFont} />
                    <input type='text' id='name' name='name' value={data.name || ''} onChange={handleInputChange} />
                </div>
                <div className='bar'></div>
            </div>
            <div className='switch-group switch-warning'>                
                <label class='switch'>
                    <input type='checkbox' id='state' name='state' checked={isChecked} onChange={handleToggle} />
                    <span class='slider'></span>
                </label>
                <label htmlFor='state'>
                    Visible
                </label>
            </div>            
            <button type='submit' className='btn btn-sm btn-warning mt-10px' disabled={btnSubmit}><FontAwesomeIcon icon={faSave} /> Guardar</button>
        </form>
    );
};

export default Edit;
