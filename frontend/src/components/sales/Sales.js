import React, { useEffect, useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faTicket } from '@fortawesome/free-solid-svg-icons'
import Table from '../Table';
import TableBody from './TableBody';
import { Requests } from '../../assets/js/Requests';

const Sales = ({ newModal, removeModal, newAlert, removeAlert }) => {
    const [forceTableUpdate, setForceTableUpdate] = useState(false);
    const [dataStatistics, setDataStatistics] = useState({
        count_total: 0
    });
    const [btnSale, setBtnSale] = useState(
        <button 
            className='btn btn-sm btn-primary'
            disabled
        >
            <FontAwesomeIcon icon={faTicket} /> Ticket
        </button>
    );

    const columnsTable = {
        'id': 'ID',
        'total': 'Total',
        'users.username': 'Caja',
        'date_reg': 'Fecha de registro',
    };
      
    const reloadTable = () => {
        setForceTableUpdate(prevState => !prevState);
    };   

    useEffect(() => {
        const setStatistics = async () => {
            const response = await Requests({ endpoint: '/sales', method: 'GET', data: {query: 'statistics'} });
            if (response.data) {
                setDataStatistics({
                    count_total: response.data.count_total
                });
            }
        };

        setStatistics();
    }, [forceTableUpdate]);

    return (
        <div>
            <div className='info-bar'>
                <h3>Ventas</h3>
                <ul>
                    <li>Administracion</li>
                    <li className='active'>/</li>
                    <li className='active'>Ventas</li>
                </ul>
            </div>        
            <div className='body g-8px'>
                <div className='grid-3 g-6px'>
                    <div className='info-panel'>
                        <div className='bar'></div>
                        <div className='info'>
                            <div className='icon'>
                                <FontAwesomeIcon icon={faTicket} />
                            </div>
                        </div>
                        <div className='data'>
                            <h2>{dataStatistics.count_total}</h2>
                            <span>Total</span>
                        </div>
                    </div>
                </div>
                <div className='grid-t-4-1 g-6px'>
                    <div className='panel'>
                        <div className='header'>
                            <h3 className='title'>Ventas</h3>
                        </div>
                        <div className='body'>
                            <Table 
                                key={forceTableUpdate} 
                                endpoint={'/sales'} 
                                columns={columnsTable} 
                                tbody={
                                    <TableBody 
                                        setBtnSale={setBtnSale}
                                        newModal={newModal} 
                                        removeModal={removeModal} 
                                        newAlert={newAlert} 
                                        removeAlert={removeAlert} 
                                        reloadTable={reloadTable}
                                    />
                                } 
                            />
                        </div>
                    </div>
                    <div className='panel'>
                        <div className='header'>
                            <h3 className='title'>Acciones</h3>
                        </div>
                        <div className='body row pt-8px pb-8px g-4px'>
                            {btnSale}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Sales;