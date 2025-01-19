import "../styles/ResultDashboard.css";
import SolutionMatrix from "./SolutionMatrix";

function ResultDashboard({result}) {



    return(
        <div className='result-dashboard-container'>
            {result ? 
                <div>
                    <SolutionMatrix result={result}/>
                </div>
                : 'Hello'
            }
        </div>        
    );
}

export default ResultDashboard;