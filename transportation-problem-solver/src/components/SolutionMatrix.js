import "../styles/SolutionMatrix.css";

function SolutionMatrix({result}) {

    return(
        <div className='solution-matrix-container'>
            <div> Number of Iterations: {result.iterations} </div>
            <div className='solution-matrix'>
                <div className='destination-names-row'>
                    <div></div>
                    {result.received.data.demands.map((item, index) =>
                        <div className='destination-name' key={index}>
                            <div>Destination {index}</div>
                        </div>
                    )}
                    <div><b>Supply</b></div>
                </div>
                {result.received.data.supplies.map((item, index) =>
                    <div className='source-row' key={index}>
                        <div className='source-name'>
                            <div>Source {index}</div>
                        </div>
                        {result.optimal_solution[index].map((item, idx) =>
                            <div key={idx}>
                                <div className='cost'> 
                                    {item}
                                </div>
                            </div>
                        )}
                        <div className='input'>
                            {result.received.data.supplies[index]}
                        </div>
                    </div>
                )}
                <div className='demand-row'>
                    <div><b>Demand</b></div>
                    {result.received.data.demands.map((item, index) =>
                        <div className='input' key={index}>
                            {item}
                        </div>
                    )}
                    <div></div>
                </div>
            </div>
        </div>        
    );
}

export default SolutionMatrix;