import MachineCycleTimeCard from './MachineCycleTimeCard'
import './ProductionRoomAccordionItem.css'

function ProductionRoomAccordionItem({roomName, roomData, openModal, machineStatuses, monitorActiveWorks, selectedAccordion, handleClick}) {
    
  return (
      <div className='acc-item' onClick={()=>handleClick(roomName)}>
        <h3 className='acc-heading'>
        <span className='acc-room-name'>{roomName}</span>
        <img className="acc-chevron" src="https://svgshare.com/i/zQr.svg"></img>
        </h3>
        
        <div className={selectedAccordion==roomName ? 'accordion-content selected' :'accordion-content'}>
          <div className='grid grid--4-cols'>{roomData.map((machine) =>
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
        </div>
      </div>
      )
}

export default ProductionRoomAccordionItem;
