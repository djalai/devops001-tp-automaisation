import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
    const [data, setData] = useState('');

    useEffect(() => {
        axios.get(`${process.env.REACT_APP_BACKEND_URL}/`)
            .then(response => setData(response.data.message))
            .catch(error => console.error('Error:', error));
    }, []);

    return (
        <div>
            <h1>Application React avec Backend Python</h1>
            <p>{data}</p>
        </div>
    );
}

export default App;

