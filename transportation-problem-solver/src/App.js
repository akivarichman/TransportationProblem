import { useState, useEffect } from 'react'
import './App.css';
import Form from './components/Form'
import ResultDashboard from './components/ResultDashboard';
// import Connection from './components/Connection'
// import PDFViewer from './components/PDFViewer';

// To Do:
// 1. pdf insert
// 2. Create diff tests / test scenarios

function App() {

    const[result, setResult] = useState('');

    return (
        <div className='page'>
        <div className='heading'>
            <span>T</span>
            <span>r</span>
            <span>a</span>
            <span>n</span>
            <span>s</span>
            <span>p</span>
            <span>o</span>
            <span>r</span>
            <span>t</span>
            <span>a</span>
            <span>t</span>
            <span>i</span>
            <span>o</span>
            <span>n</span>
            <span> </span>
            <span>P</span>
            <span>r</span>
            <span>o</span>
            <span>b</span>
            <span>l</span>
            <span>e</span>
            <span>m</span>
            <span> </span>
            <span>S</span>
            <span>o</span>
            <span>l</span>
            <span>v</span>
            <span>e</span>
            <span>r</span>
        </div>
        <Form setResult={setResult}/>
        <ResultDashboard result={result}/>
        </div>
    );
}

export default App;
