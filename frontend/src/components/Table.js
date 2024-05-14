import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faAngleDoubleLeft, faAngleDoubleRight, faAngleLeft, faAngleRight, faSearch, faSortDown, faSortUp } from '@fortawesome/free-solid-svg-icons';
import { applyInputEffects } from '../assets/js/script';
import configData from '../config.json';

const Table = ({ endpoint, columns, tbody, query_name = 'table'}) => {
    const [data, setData] = useState([]);
    const [tableData, setTableData] = useState({
        query: query_name,
        search: '',
        page: 1,
        order_by: 'id',
        order: 'asc',
        show: 10
    });
    const [totalPages, setTotalPages] = useState(1);

    const maxButtonsToShow = 5;

    useEffect(() => {
        const authToken = localStorage.getItem('authToken');
        applyInputEffects();

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

        axios.get(url,
        { 
            headers: {
                'Authorization': `Bearer ${authToken}`
            }
        }).then(response => {
            setData(response.data.data);
            setTotalPages(response.data.total_pages);
        }).catch(error => {
            console.error('Error fetching data: ', error);
        });
    }, [tableData, endpoint]);

    const handleInputChange = event => {
        const { name, value } = event.target;
        setTableData({ ...tableData, [name]: value, page: 1 });
    };

    const handlePageChange = newPage => {
        setTableData({ ...tableData, page: newPage });
    };

    const handleFirstPage = () => {
        handlePageChange(1);
    };

    const handleLastPage = () => {
        handlePageChange(totalPages);
    };

    const handleNextPage = () => {
        if (tableData.page < totalPages) {
            handlePageChange(tableData.page + 1);
        }
    };

    const handlePrevPage = () => {
        if (tableData.page > 1) {
            handlePageChange(tableData.page - 1);
        }
    };

    const handleSort = column => {
        const newOrder = tableData.order_by === column && tableData.order === 'asc' ? 'desc' : 'asc';
        setTableData({ ...tableData, order_by: column, order: newOrder });
    };

    const renderPaginationButtons = () => {
        const buttons = [];
        let startPage = Math.max(1, tableData.page - Math.floor(maxButtonsToShow / 2));
        const endPage = Math.min(totalPages, startPage + maxButtonsToShow - 1);

        if (totalPages - tableData.page < Math.floor(maxButtonsToShow / 2)) {
            startPage = Math.max(1, totalPages - maxButtonsToShow + 1);
        }

        for (let i = startPage; i <= endPage; i++) {
            buttons.push(
                <button
                    className={`btn btn-primary ${tableData.page === i ? 'active' : ''}`}
                    key={i}
                    onClick={() => handlePageChange(i)}
                >
                    {i}
                </button>
            );
        }

        return buttons;
    };

    return (
        <div className='table-content'>
            <div className='table-search'>
                <div className='search input-group'>                
                    <div className='input'>
                        <label htmlFor='search'>Busqueda</label>
                        <FontAwesomeIcon icon={faSearch} />
                        <input type='text' id='search' name='search' value={tableData.name} onChange={handleInputChange}  />
                    </div>
                    <div className='bar'></div>
                </div>
            </div>
            <div className='table-responsive mt-12px'>
                <table>
                    <thead>
                        <tr>
                            {Object.keys(columns).map((fieldName) => (
                                <th key={fieldName} onClick={() => handleSort(fieldName)}>
                                    {columns[fieldName]}{' '}
                                    {tableData.order_by === fieldName && (
                                    tableData.order === 'asc' ? <FontAwesomeIcon icon={faSortUp} /> : <FontAwesomeIcon icon={faSortDown} />
                                    )}
                                </th>
                            ))}
                        </tr>
                    </thead>
                    {React.cloneElement(tbody, { data: data })} 
                </table>
            </div>
            <div className='table-pagination'>
                <div>
                    Mostrando {tableData.show}, página {tableData.page} de {totalPages}.
                </div>
                <div className='pagination'>
                    <button className='btn btn-primary' onClick={handleFirstPage}><FontAwesomeIcon icon={faAngleDoubleLeft} /></button>
                    <button className='btn btn-primary' onClick={handlePrevPage}><FontAwesomeIcon icon={faAngleLeft} /></button>
                    {totalPages <= maxButtonsToShow ?
                        renderPaginationButtons() :
                        tableData.page <= Math.floor(maxButtonsToShow / 2) + 1 ?
                            renderPaginationButtons().slice(0, maxButtonsToShow) :
                            renderPaginationButtons().slice(-maxButtonsToShow)
                    }
                    <button className='btn btn-primary' onClick={handleNextPage}><FontAwesomeIcon icon={faAngleRight} /></button>
                    <button className='btn btn-primary' onClick={handleLastPage}><FontAwesomeIcon icon={faAngleDoubleRight} /></button>
                </div>
            </div>
        </div>
    );
};

export default Table;