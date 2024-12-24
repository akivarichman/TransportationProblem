import { useState, useEffect } from 'react'

function Connection() {
    const [message, setMessage] = useState('');

    useEffect(() => {
      // GET request to fetch data
      fetch('http://localhost:5000/api/data')
        .then((response) => response.json())
        .then((data) => setMessage(data.message))
        .catch((error) => console.error('Error:', error));
    }, []);
  
    const sendData = () => {
      // POST request to send data
      fetch('http://localhost:5000/api/data', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ key: 'value' }),
      })
        .then((response) => response.json())
        .then((data) => {console.log('Response:', data)})
        .catch((error) => console.error('Error:', error));
    };
  
    return (
      <div>
        <h1>{message}</h1>
        <button onClick={sendData}>Send Data</button>
      </div>
    );
}

export default Connection;