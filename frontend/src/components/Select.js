import React, { useEffect, useState } from 'react';
import axios from 'axios';
import configData from '../config.json';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCaretRight, faFilter } from '@fortawesome/free-solid-svg-icons';

const Select = ({ name, endpoint, data, handleInputChange }) => {
    const [status, setStatus] = useState(''); 
    const [statusMenu, setStatusMenu] = useState('hidden');
    const [selectedOption, setSelectedOption] = useState('Seleccione una opcion...');
    const [result, setResult] = useState([]);
    const [tableData, setTableData] = useState({
        query: 'table',
        search: '',
        page: 1,
        order_by: 'id',
        order: 'asc',
        show: 10
    });
    const [totalPages, setTotalPages] = useState(1);

    const handleActive = () => {
        if (status === 'active') {
            setStatus('');
            setTimeout(() => {
                setStatusMenu('hidden');
            }, 450);
        } else {
            setStatusMenu('');
            setTimeout(() => {
                setStatus('active');
            }, 250);
        }
    }

    const handleOptionClick = (value, option) => {
        setSelectedOption(option);
        handleInputChange({ target: { name: name, value: value } });
        handleActive();
    }

    useEffect(() => {
        let url = `${configData.api_url}${endpoint}`;
        const params = new URLSearchParams();

        for (const [key, value] of Object.entries(tableData)) {
          if (value !== null && value !== undefined) {
            if (typeof value === 'object') {
              for (const [subKey, subValue] of Object.entries(value)) {
                params.append(`${key}[${subKey}]`, subValue);
              }
            } else {
              params.append(key, value);
            }
          }
        }

        url += `?${params.toString()}`;

        axios.get(url).then(response => {
            setResult(response.data.data);
            setTotalPages(response.data.total_pages);
        }).catch(error => {
            console.error('Error fetching data: ', error);
        });
    }, [tableData, endpoint]);

    const handleLocalInputChange = event => {
        const { name, value } = event.target;
        setTableData({ ...tableData, [name]: value, page: 1 });
    };

    return (
        <div className={`select-group mt-4px ${status}`}>
            <div className='select' onClick={handleActive}>
                <span className='option'><FontAwesomeIcon icon={faFilter} /> {selectedOption}</span> <FontAwesomeIcon className='left' icon={faCaretRight} />
            </div>
            <input className='input' name={name} value={data[name] || ''} onChange={handleInputChange} />
            <div className={`select-menu ${statusMenu}`}>
                <input id='search' name='search' placeholder='Busqueda...' value={tableData.name} onChange={handleLocalInputChange} />
                <ul>
                    <li onClick={() => handleOptionClick(0, 'Seleccione una opcion...')}>
                        Seleccione una opcion...
                    </li>
                    {result.map((entry, index) => (
                        <li onClick={() => handleOptionClick(entry.id, entry.name)}>
                            {entry.name}
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default Select;
