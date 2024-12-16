import { useState, useEffect } from 'react'
import "../styles/Form.css";
import { IoMdRemoveCircleOutline } from "react-icons/io";

// Next To Do:

function Form() {

    const[numberOfSources, setNumberOfSources] = useState(3)
    const[numberOfDestinations, setNumberOfDestinations] = useState(3)
    const[supplyInputs, setSupplyInputs] = useState(['', '', ''])
    const[demandInputs, setDemandInputs] = useState(['', '', ''])
    const[costInputs, setCostInputs] = useState([['', '', ''], ['', '', ''], ['', '', '']])

    const handleSubmit = (event) => {
        event.preventDefault();
        const formData = {
            supplies: [...supplyInputs],
            demands: [...demandInputs],
            costs: [...costInputs],
        };
        if(isFormDataValid(formData)) {
            console.log('form data is valid');
        } else {
            console.log('error');
        }
    }

    const isFormDataValid = (data) => {
        return(
            // all supply inputs are positive
            data.supplies.every((value) => value !== null && value !== '' && value > 0) &&
            // all demand inputs are positive
            data.demands.every((value) => value !== null && value !== '' && value > 0) &&
            // all cost inputs are greater than or equal to zero
            data.costs.every((row) => row.every((value) => value !== null && value !== '' && value >= 0)) &&
            // supply is equal to demand
            (data.supplies.reduce((sum, value) => sum + Number(value || 0), 0) === data.demands.reduce((sum, value) => sum + Number(value || 0), 0))
        );
    }

    // do I even need handleInputChange? cant I just store the values in handleSubmit?
    const handleInputChange = (event, index, idx) => {
        if(event.target.name === 'supply') {
            const updatedInputs = [...supplyInputs];
            updatedInputs[index] = event.target.value;
            setSupplyInputs(updatedInputs);
        }
        else if(event.target.name === 'demand') {
            const updatedInputs = [...demandInputs];
            updatedInputs[index] = event.target.value;
            setDemandInputs(updatedInputs);
        }
        else if(event.target.name === 'cost') {
            const updatedInputs = [...costInputs];
            updatedInputs[index][idx] = event.target.value;
            setCostInputs(updatedInputs);
        }
    }

    useEffect(() => {
        console.log('Supply: ', supplyInputs);
    }, [supplyInputs]);

    useEffect(() => {
        console.log('Demand: ', demandInputs);
    }, [demandInputs]);

    useEffect(() => {
        console.log('Costs: ', costInputs);
    }, [costInputs]);

    const handleAddSourceButtonClick = (event) => {
        const num = numberOfSources + 1
        setNumberOfSources(num)
        setSupplyInputs([...supplyInputs, ''])
        setCostInputs(costInputs => [
            ...costInputs,
            new Array(numberOfDestinations).fill('')
        ]);
    }

    const handleAddDestinationButtonClick = (event) => {
        const num = numberOfDestinations + 1
        setNumberOfDestinations(num)
        setDemandInputs([...demandInputs, ''])
        setCostInputs(costInputs => 
            costInputs.map(subArray => [...subArray, ''])
        );
    }

    const handleRemoveSourceClick = (indexToRemove) => {
        const num = numberOfSources - 1
        setNumberOfSources(num)

        const newSupplyInputs = [...supplyInputs]
        newSupplyInputs.splice(indexToRemove, 1)
        setSupplyInputs(newSupplyInputs)

        const newCostInputs = [...costInputs]
        newCostInputs.splice(indexToRemove, 1)
        setCostInputs(newCostInputs)
    }

    const handleRemoveDestinationClick = (indexToRemove) => {
        const num = numberOfDestinations - 1
        setNumberOfDestinations(num)

        const newDemandInputs = [...demandInputs]
        newDemandInputs.splice(indexToRemove, 1)
        setDemandInputs(newDemandInputs)

        const newCostInputs = costInputs.map(subArray => {
            const newSubArray = [...subArray]
            newSubArray.splice(indexToRemove, 1)
            return newSubArray
        })
        setCostInputs(newCostInputs)
    }
    

    return(
        <div>
            <div class='form-container'>
                <form onSubmit={handleSubmit}>
                    <div class='destination-names-row'>
                        <div></div>
                        {demandInputs.map((item, index) =>
                            <div class='destination-name'>
                                <div>New Destination {index}</div>
                                {(index > 1) && <div class='remove-button' onClick={(event) => handleRemoveDestinationClick(index)}><IoMdRemoveCircleOutline/></div>}
                            </div>
                        )}
                        <div><b>Supply</b></div>
                    </div>
                    {supplyInputs.map((item, index) =>
                        <div class='source-row'>
                            <div class='source-name'>
                                <div>New Source {index}</div>
                                {(index > 1) && <div class='remove-button' onClick={(event) => handleRemoveSourceClick(index)}><IoMdRemoveCircleOutline/></div>}
                            </div>
                            {costInputs[index].map((item, idx) =>
                                <div>
                                    <div class='input'> 
                                        <input type='number' name='cost' min='0' value={costInputs[index][idx]} onChange={(event) => handleInputChange(event, index, idx)} required></input> 
                                    </div>
                                </div>
                            )}
                            <div class='input'>
                                <input type='number' name='supply' min='0' value={supplyInputs[index]} onChange={(event) => handleInputChange(event, index)} required></input>
                            </div>
                        </div>
                    )}
                    <div class='demand-row'>
                        <div><b>Demand</b></div>
                        {demandInputs.map((item, index) =>
                            <div class='input'>
                                <input type='number' name='demand' min='0' value={demandInputs[index]} onChange={(event) => handleInputChange(event, index)} required></input>
                            </div>
                        )}
                        <div></div>
                    </div>
                    <div class='buttons'>
                        <button onClick={handleAddSourceButtonClick}>Add Source</button>
                        <button onClick={handleAddDestinationButtonClick}>Add Destination</button>
                        <input type='submit'></input>
                    </div>
                </form>
            </div>
            
        </div>        
    );
}

export default Form;