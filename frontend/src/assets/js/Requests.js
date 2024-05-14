import axios from 'axios';
import configData from '../../config.json';


export const Requests = async ({ endpoint, method = 'POST', data = null }) => {
    let response = {
        code: null,
        data: null,
    };

    try {
        const authToken = localStorage.getItem('authToken');
        let res = null;

        if(method === 'GET'){
            const params = new URLSearchParams();

            for (const [key, value] of Object.entries(data)) {
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
            let url = `${configData.api_url}${endpoint}`
            url += `?${params.toString()}`;
            res = await axios.get(
                url,
                { 
                    headers: {
                        'Authorization': `Bearer ${authToken}`
                    }
                }
            );          
        } else if(method === 'POST'){               
            res = await axios.post(
                `${configData.api_url}${endpoint}`, data
            );           
        }

        response.code = res.status;
        response.data = res.data;
    } catch (error) {
        response.code = error.response.status;
        response.data = error.response.data;
    }

    return response;
};