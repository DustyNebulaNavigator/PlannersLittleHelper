import './MachineCycleTimeCard.css'

function MachineCycleTimeCard({machine_name, cycle_time}){
    return (
        <div className="machine-card">
            <h3 className="machine-name">{machine_name}</h3>
            <p className="cycle-time">{cycle_time}</p>    
        </div>
        )
}

export default MachineCycleTimeCard;