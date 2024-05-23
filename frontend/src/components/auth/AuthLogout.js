import { useEffect } from 'react';

const AuthLogout = ({ setAuth }) => {
    useEffect(() => {
        localStorage.removeItem('authToken');
        setAuth(false); 
      });
    return;
};

export default AuthLogout;
