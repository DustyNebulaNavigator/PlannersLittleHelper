import { useEffect, useState } from 'react'

import MachineCycleTimeCard from './MachineCycleTimeCard'

function CycleTimesPage (){
    const [data, setData] = useState([])
    const [machineStatuses, setmachineStatuses] = useState([])
  
  useEffect( () => {
    // Cycle time fetching
    async function fetchCycleTimes() {
      try {
        const response = await fetch(`${import.meta.env.VITE_API_URL}cycletimes`)
        if (!response.ok) {
          throw new Error('Network response not ok')
        }
        const result = await response.json();
        setData(result)
      } catch (error) {
        console.log('Error fetching data:', error)
      }}
      fetchCycleTimes()
      // Machine statuses fetching
    async function fetchStatuses() {
      try{
        const response = await fetch(`${import.meta.env.VITE_API_URL}statuses`)
        if (!response.ok) {
          throw new Error('Network response not ok')
        }
        const result = await response.json();
        setmachineStatuses(result)
      }catch (error) {
        console.log('Error fetching data:', error)
      }
    }
    fetchStatuses()
  },[])
    
    return <div className='grid grid--4-cols'>{data.map((machine) =><MachineCycleTimeCard machine_name={machine.machine_name} cycle_time={machine.cycle_time} statuses={machineStatuses} key={machine.machine_name}/>)}</div>
}

export default CycleTimesPage