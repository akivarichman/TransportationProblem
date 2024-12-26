import { useState, useEffect } from 'react'
import "../styles/ResultDashboard.css";

function ResultDashboard({result}) {



    return(
        <div className='result-dashboard-container'>
            Hello
            {JSON.stringify(result)}
        </div>        
    );
}

export default ResultDashboard;