import { useEffect, useState, useRef } from 'react'

import MachineCycleTimeCard from './MachineCycleTimeCard'
import MachineCycleTimeModal from './MachineCycleTimeModal'


function CycleTimesPage (){
    const [data, setData] = useState([])
    const [machineStatuses, setmachineStatuses] = useState([])
    const [monitorActiveWorks, setMonitorActiveWorks] = useState([])
    // States for modal - Chart with machine cycle times
    const [selectedMachine, setSelectedMachine] = useState(null)
    const [selectedMachineData, setSelectedMachineData] = useState(null)

    // Fetches machine cycle time data to display on MachineCycleTimeModal
    async function fetchMachineHistoricData(lookback_days=1, interval_minutes=20){
      if (!selectedMachine) return;

      try {
        const response = await fetch(`${import.meta.env.VITE_API_URL}macinecyclestats/?machine_name=${selectedMachine}&lookback_days=${lookback_days}&interval_minutes=${interval_minutes}`)
        
        if (!response.ok) {
          throw new Error('Network response not ok')
        }
        const result = await response.json();
        setSelectedMachineData(result);
      } catch (error) {
        console.log('Error fetching data:', error)
      }
    }
    
    // Runs every time selectedMachine changes
    useEffect(()=>{
      fetchMachineHistoricData();
    }, [selectedMachine])

    async function openModal (machine) {
      setSelectedMachine(machine);
    }

    
    function closeModal (){
      setSelectedMachine(null);
      setSelectedMachineData(null);
    }
    
  
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

    async function fetchMonitorActiveWorks() {
      try{
        const response = await fetch(`${import.meta.env.VITE_API_URL}partNr/monitor_cycle_times/`)
        if (!response.ok) {
          throw new Error('Network response not ok partNr/monitor_cycle_times/')
        }
        const result = await response.json();
        setMonitorActiveWorks(result)
      }catch (error) {
        console.log('Error fetching data:', error)
      }
    }
    fetchMonitorActiveWorks()

  },[])
    
    return (
      <>
        <div className='grid grid--4-cols'>{data.map((machine) =>
          <MachineCycleTimeCard 
            hangleMachineClick={openModal}
            machine_name={machine.machine_name} 
            machine_cycle_time={machine.cycle_time} 
            statuses={machineStatuses}
            monitorActiveWorks={monitorActiveWorks}
            key={machine.machine_name}
          />
          )}
        </div>
        {selectedMachine && (
          <MachineCycleTimeModal onClose={closeModal} data={selectedMachineData} machineName={selectedMachine} handleSubmit={fetchMachineHistoricData}/>
        )}
        
        
      </>)
}

export default CycleTimesPage