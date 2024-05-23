import React, { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBasketShopping, faCheckCircle, faTimes } from '@fortawesome/free-solid-svg-icons';
import Table from '../Table';
import TableBody from './TableBody';
import Modal from '../Modal';
import EditCart from './EditCart';
import FinalizeCart from './FinalizeCart';

const AppPos = ({ newModal, removeModal, newAlert, removeAlert }) => {
    const [forceTableUpdate, setForceTableUpdate] = useState(false);    
    const cartSaved = localStorage.getItem('cart');
    const cartStart = cartSaved ? JSON.parse(cartSaved) : [];
    const [cart, setCart] = useState(cartStart);
    
    const columnsTable = {
        'id': 'ID',
        'name': 'Nombre',
        'description': 'Descripcion',
        'price': 'Precio',
        'product_categories.name': 'Categoria'
    };

    const reloadTable = () => {
        setForceTableUpdate(prevState => !prevState);
    };

    const addToCart = (product) => {
        const existingIndex = cart.findIndex(item => item.id === product.id);
        if (existingIndex !== -1) {
            const newCart = [...cart];
            newCart[existingIndex].quantity += parseFloat(product.quantity);
            setCart(newCart);
            localStorage.setItem('cart', JSON.stringify(newCart));
        } else {
            const newProduct = { ...product, quantity: parseFloat(product.quantity) };
            const newCart = [...cart, newProduct];
            setCart(newCart);
            localStorage.setItem('cart', JSON.stringify(newCart));
        }
    };
    
    const editToCart = (product) => {
        const quantity = parseFloat(product.quantity);
        if (quantity > 0) {
            const existingIndex = cart.findIndex(item => item.id === product.id);
            if (existingIndex !== -1) {
                const newCart = [...cart];
                newCart[existingIndex].quantity = quantity;
                if (quantity === 0) {
                    newCart.splice(existingIndex, 1);
                }
                setCart(newCart);
                localStorage.setItem('cart', JSON.stringify(newCart));
            }
        } else {
            const existingIndex = cart.findIndex(item => item.id === product.id);
            if (existingIndex !== -1) {
                const newCart = [...cart];
                newCart.splice(existingIndex, 1);
                setCart(newCart);
                localStorage.setItem('cart', JSON.stringify(newCart));
            }
        }
    };

    const clearCart = () => {
        setCart([]);
        localStorage.removeItem('cart');
    };

    const calculateTotal = () => {
        let total = 0;
        cart.forEach(item => {
            total += item.price * item.quantity;
        });
        return total;
    };

    const handleEdit = (item) => {
        newModal({
            'id': `app-cart-finalize-${item.id}-modal`,
            'app':
                <Modal
                    key={`app-cart-finalize-${item.id}-modal`}
                    id={`app-cart-finalize-${item.id}-modal`}
                    color={'warning'}
                    title={'Editar el carrito'}
                    body={
                        <EditCart item={item} editToCart={editToCart} newAlert={newAlert} removeAlert={removeAlert}/>
                    }
                    removeModal={removeModal}
                />
        });
    };

    const handleFinalize = () => {
        newModal({
            'id': `app-cart-finalize-modal`,
            'app':
                <Modal
                    key={`app-cart-finalize-modal`}
                    id={`app-cart-finalize-modal`}
                    color={'primary'}
                    title={'Finalizar el carrito'}
                    body={
                        <FinalizeCart cart={cart} clearCart={clearCart} newAlert={newAlert} removeAlert={removeAlert}/>
                    }
                    removeModal={removeModal}
                />
        });
    };

    return (
        <div>
            <div className='info-bar'>
                <h3>Punto de venta</h3>
                <ul>
                    <li>App</li>
                    <li className='active'>/</li>
                    <li className='active'>Punto de venta</li>
                </ul>
            </div>
            <div className='body g-8px'>
                <div className='grid-t-3-1 g-6px'>
                    <div className='row column g-6px'>                    
                        <div className='panel'>
                            <div className='header'>
                                <h3 className='title'>Productos</h3>
                            </div>
                            <div className='body'>
                                <Table
                                    key={forceTableUpdate}
                                    endpoint={'/products'}
                                    columns={columnsTable}
                                    tbody={
                                        <TableBody
                                            addToCart={addToCart}
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
                    </div>
                    <div className='row column g-6px'>      
                        <div className='panel'>
                            <div className='header'>
                                <h3 className='title'>Ticket</h3>
                            </div>
                            <div className='body row pt-8px pb-8px g-4px'>
                                {
                                    cart.length > 0 ? 
                                        cart.map((item, index) => (
                                            <div key={index} className='card-cart' onClick={() => handleEdit(item)}>
                                                <div className='icon'>
                                                    <FontAwesomeIcon icon={faBasketShopping} />
                                                </div>
                                                <div className='product'>
                                                    <h3>{ item.name }</h3>
                                                    <p>{ item.product_categories.name }</p>
                                                </div>
                                                <div className='price g-4px'>
                                                    <h3>${ item.price }</h3> <span>x</span> <span>{ item.quantity }</span>
                                                </div>
                                                <div className='total g-4px'>
                                                    <h3>${ item.price * item.quantity }</h3>
                                                </div>
                                            </div>
                                        ))                                    
                                    : 
                                    <div className='card-cart'>
                                        <div className='icon'>
                                            <FontAwesomeIcon icon={faTimes} />
                                        </div>
                                        <div className='product'>
                                            <h3>Nada en el carrito</h3>
                                            <p>Sin productos</p>
                                        </div>
                                        <div className='price g-4px'></div>
                                        <div className='total g-4px'></div>
                                    </div>
                                }
                                
                                <div className='row justify-content-end cart-total'>
                                    <h2>${calculateTotal()}</h2>
                                </div>                            
                            </div>
                        </div>
                        <div className='panel'>
                            <div className='header'>
                                <h3 className='title'>Actions</h3>
                            </div>
                            <div className='body row pt-8px pb-8px g-4px'>
                            <button 
                                className='btn btn-sm btn-primary' 
                                onClick={handleFinalize}
                            >
                                <FontAwesomeIcon icon={faCheckCircle} /> Finalizar
                            </button>                          
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default AppPos;