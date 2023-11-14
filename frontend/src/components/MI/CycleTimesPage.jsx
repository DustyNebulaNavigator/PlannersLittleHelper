import { useEffect, useState, useRef } from 'react'


import MachineCycleTimeModal from './MachineCycleTimeModal'
import ProductionRoomAccordionItem from './ProductionRoomAccordionItem'


function CycleTimesPage (){
    const [data, setData] = useState([])
    const [data_sv1, setData_sv1] = useState([])
    const [data_sv2, setData_sv2] = useState([])
    const [data_sv3, setData_sv3] = useState([])
    const [selectedAccordion, setSelectedAccordion] = useState("Survevalu 1")
    const [machineStatuses, setmachineStatuses] = useState([])
    const [monitorActiveWorks, setMonitorActiveWorks] = useState([])
    // States for modal - Chart with machine cycle times
    const [selectedMachine, setSelectedMachine] = useState(null)
    const [selectedMachineData, setSelectedMachineData] = useState(null)

    const machines_in_room_sv1 = ['M0222', 'M0301', 'M0091', 'M0422', 'M0153', 'M0281', 'M0402', 'M0501', 'M0221', 'M0202', 'M0901', 'M1002', 'M0201', 'M0253', 'M0451', 'M0352', 'M1003', 'M0131', 'M0273']
    const machines_in_room_sv2 = ['M0057', 'M0082', 'M0044', 'M0025', 'M0055', 'M0083', 'M0054', 'M0056', 'M0042', 'M0051', 'M0035', 'M0081', 'M0084']
    const machines_in_room_sv3 = ['M0041', 'M0102', 'M0052', 'M0123', 'M0101', 'M0122', 'M0121', 'M0151']

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

    function handleAccordionClick(machineName) {
      setSelectedAccordion(machineName)
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

  // When status has changed update room specific lists
  useEffect(()=>{
    setData_sv1(data.filter((machine)=>machines_in_room_sv1.includes(machine.machine_name)))
    setData_sv2(data.filter((machine)=>machines_in_room_sv2.includes(machine.machine_name)))
    setData_sv3(data.filter((machine)=>machines_in_room_sv3.includes(machine.machine_name)))
  }, [data]

  )
    
    return (
      <>
        <div className='accordion'>
          <ProductionRoomAccordionItem roomName="Survevalu 1" roomData={data_sv1} openModal={openModal} machineStatuses={machineStatuses} monitorActiveWorks={monitorActiveWorks} selectedAccordion={selectedAccordion} handleClick={handleAccordionClick} />
          <ProductionRoomAccordionItem roomName="Survevalu 2" roomData={data_sv2} openModal={openModal} machineStatuses={machineStatuses} monitorActiveWorks={monitorActiveWorks} selectedAccordion={selectedAccordion} handleClick={handleAccordionClick} />
          <ProductionRoomAccordionItem roomName="Survevalu 3" roomData={data_sv3} openModal={openModal} machineStatuses={machineStatuses} monitorActiveWorks={monitorActiveWorks} selectedAccordion={selectedAccordion} handleClick={handleAccordionClick} />
        </div>
        {selectedMachine && (
          <MachineCycleTimeModal onClose={closeModal} data={selectedMachineData} machineName={selectedMachine} handleSubmit={fetchMachineHistoricData}/>
        )}
        
        
      </>)
}

export default CycleTimesPage