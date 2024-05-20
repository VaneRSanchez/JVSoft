import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCalendar, faFingerprint, faTicket } from '@fortawesome/free-solid-svg-icons'
import { useNavigate } from 'react-router-dom';

const TableBody = ({ data, setBtnSale, newModal, removeModal, newAlert, removeAlert, reloadTable }) => {  
    const navigate = useNavigate();
    
    const handleEdit = (entry) => {
        navigate(`/pdf/sale?id=${entry.id}`);

        setBtnSale( 
            <button 
                className='btn btn-sm btn-primary'
                disabled
            >
                <FontAwesomeIcon icon={faTicket} /> Ticket
            </button>
        );
    };  

    const handleClick = (entry) => {
        setBtnSale(
            <button 
                className='btn btn-sm btn-primary' 
                onClick={() => handleEdit(entry)}
            >
                <FontAwesomeIcon icon={faTicket} /> Ticket
            </button>
        );
    };  

    return (
        <tbody>
            {data.map((entry, index) => (
                <tr 
                    key={index}
                    onClick={() => handleClick(entry)}
                >
                    <td><span className='badge'><FontAwesomeIcon icon={faFingerprint} /> {entry.id}</span></td>
                    <td>${entry.total}</td>
                    <td>{entry.users.username}</td>
                    <td><span className='badge'><FontAwesomeIcon icon={faCalendar} /> {entry.date_reg}</span></td>
                </tr>
            ))}
        </tbody>
    );
};

export default TableBody;
