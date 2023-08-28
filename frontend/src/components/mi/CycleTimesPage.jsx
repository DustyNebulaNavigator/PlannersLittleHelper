import { useEffect, useState } from 'react'

import MachineCycleTimeCard from './MachineCycleTimeCard'

function CycleTimesPage (){
    const [data, setData] = useState([])
  
  useEffect( () => {
    async function fetchData() {
      try {
        const response = await fetch(`${import.meta.env.VITE_API_URL}cycletimes`)
        if (!response.ok) {
          throw new Error('Network response not ok')
        }
        const result = await response.json();
        setData(result)
        console.log(result)
      } catch (error) {
        console.log('Error fetching data:', error)
      }}
      fetchData()
  },[])
    
    return <div className='grid grid--4-cols'>{data.map((machine) =><MachineCycleTimeCard machine_name={machine.machine_name} cycle_time={machine.cycle_time} key={machine.machine_name}/>)}</div>
}

export default CycleTimesPage