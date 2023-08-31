import { useState } from 'react';

import './GetPartById.css'

export default function GetPartById (){
    const [partId, setPartId] = useState("")
    const [partNumber, setPartNumber] = useState("")
    const [partDescription, setPartDescription] = useState("")

    function handleChange (e) {
        setPartId(e.target.value)
    }

    function handleSubmit(e){
        e.preventDefault();
        async function fetchCycleTimes() {
            try {
              const response = await fetch(`${import.meta.env.VITE_API_URL}partNr/${partId}`)
              if (!response.ok) {
                throw new Error('Network response not ok')
              }
              const result = await response.json();
              setPartNumber(result[0].part_nr)
              setPartDescription(result[0].part_description)
            } catch (error) {
                setPartNumber("Please check the ID")
                setPartDescription("")
              console.log('Error fetching data:', error)
            }}
            fetchCycleTimes()
    }

    return (
        <div className='small-center-container'>
            <form onSubmit={handleSubmit} className='form'>
                <input type="text" placeholder="Part ID" onChange={handleChange} />
                <button className='btn'>Search</button>
            </form>

            <div className='response-message'>
                <p>{partNumber}</p>
                <p>{partDescription}</p>
            </div>
        </div>
    )
}