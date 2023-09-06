import './MachineCycleTimeCard.css'

function MachineCycleTimeCard({machine_name, machine_cycle_time, monitorActiveWorks, statuses}){

    const status_color = statuses.filter((status) => status.machine_name === machine_name)[0].status
    
    // Get active work on this machine, if status is green
    //let activeWork = undefined
    let monitor_cycle_time = undefined
    let isTooSlow = undefined
    if (status_color === 'green'){
        const activeWork =  monitorActiveWorks.filter(work=>work.machine_nr == machine_name)[0]
        monitor_cycle_time = parseFloat(activeWork?.unit_time.toFixed(2))
        isTooSlow = monitor_cycle_time < machine_cycle_time
    }
    return (
        <div className={`machine-card ${status_color}`}>
        <div  className="col-3 machine-name">
        <p></p>
        <h3 className="machine-name">{machine_name}</h3>
        <p className='left'>{status_color === 'green' && "⏱️"}</p>
        </div>
            {status_color==='green' &&
             <div className="cycle-time">
                <p>{monitor_cycle_time ? `${monitor_cycle_time}` : ''}</p>

                <p className={isTooSlow ? "slow-cycle-time left": "left"}>{machine_cycle_time}</p>
             </div>}
        </div>
        )
}

export default MachineCycleTimeCard;