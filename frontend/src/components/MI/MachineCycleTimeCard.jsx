import './MachineCycleTimeCard.css'

function MachineCycleTimeCard({machine_name, cycle_time, statuses}){

    const status_color = statuses.filter((status) => status.machine_name === machine_name)[0].status
  
    return (
        <div className={`machine-card ${status_color}`}>
            <h3 className="machine-name">{machine_name}</h3>
            {status_color==='green' && <p className="cycle-time">{cycle_time}</p>    }
        </div>
        )
}

export default MachineCycleTimeCard;