import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faAngleDoubleLeft, faAngleDoubleRight, faAngleLeft, faAngleRight, faSearch, faSortDown, faSortUp } from '@fortawesome/free-solid-svg-icons';
import { applyInputEffects } from '../assets/js/script';

const Table = () => {
    const [data, setData] = useState([]);
    const [tableData, setTableData] = useState({
        search: '',
        page: 1,
        order_by: 'id',
        order: 'asc',
        show: 10
    });
    const [totalPages, setTotalPages] = useState(1);

    useEffect(() => {
        applyInputEffects();

        let url = 'http://192.168.0.179:8000/api/product/categories';
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
            setData(response.data.data);
            setTotalPages(response.data.total_pages);
        }).catch(error => {
            console.error('Error fetching data: ', error);
        });
    }, [tableData]);

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
                            <th onClick={() => handleSort('id')}>
                                ID{' '}
                                {tableData.order_by === 'id' && (
                                    tableData.order === 'asc' ? <FontAwesomeIcon icon={faSortUp} /> : <FontAwesomeIcon icon={faSortDown} />
                                )}
                            </th>
                            <th onClick={() => handleSort('name')}>
                                Nombre{' '}
                                {tableData.order_by === 'name' && (
                                    tableData.order === 'asc' ? <FontAwesomeIcon icon={faSortUp} /> : <FontAwesomeIcon icon={faSortDown} />
                                )}
                            </th>
                            <th onClick={() => handleSort('status')}>
                                Estatus{' '}
                                {tableData.order_by === 'status' && (
                                    tableData.order === 'asc' ? <FontAwesomeIcon icon={faSortUp} /> : <FontAwesomeIcon icon={faSortDown} />
                                )}
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        {data.map((entry, index) => (
                            <tr key={index}>
                                <td>{entry.id}</td>
                                <td>{entry.name}</td>
                                <td>{entry.status}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
            <div className='table-pagination'>
                <div>
                    Mostrando {tableData.show}, página {tableData.page} de {totalPages}.
                </div>
                <div className='pagination'>
                    <button className='btn btn-primary' onClick={handleFirstPage}><FontAwesomeIcon icon={faAngleDoubleLeft} /></button>
                    <button className='btn btn-primary' onClick={handlePrevPage}><FontAwesomeIcon icon={faAngleLeft} /></button>
                    {Array.from({ length: totalPages }, (_, index) => (
                        <button
                            className={`btn btn-primary ${tableData.page === index + 1 ? 'active' : ''}`}
                            key={index}
                            onClick={() => handlePageChange(index + 1)}
                        >
                            {index + 1}
                        </button>
                    ))}
                    <button className='btn btn-primary' onClick={handleNextPage}><FontAwesomeIcon icon={faAngleRight} /></button>
                    <button className='btn btn-primary' onClick={handleLastPage}><FontAwesomeIcon icon={faAngleDoubleRight} /></button>
                </div>
            </div>
        </div>
    );
};

export default Table;
