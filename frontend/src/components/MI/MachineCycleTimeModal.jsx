import { useEffect, useState, useRef } from 'react';
import { useLocation } from 'react-router-dom';
import {CartesianGrid, Legend, Line, LineChart, Tooltip, XAxis, YAxis} from "recharts";

import './MachineCycleTimeModal.css'

export default function MachineCycleTimeModal ({machineName, data, onClose, handleSubmit}){
  const [lookbackDays, setlookbackDays] = useState(1)
  const [intervalMinutes, setintervalMinutes] = useState(20)
  let chartRef = useRef();

  // If mousedown is outside modal - on background, then closes modal
  useEffect(()=>{
    let handler = (e)=>{
      if(!chartRef.current.contains(e.target)){
        onClose()
      }
    };
    document.addEventListener("mousedown", handler);
    return()=>document.removeEventListener("mousedown",handler)
  })

  function handleLookbackDayChange(e) {
    const inputValue = e.target.value;
    if (/^(\d+\.?\d*|\.\d+)$/.test(inputValue) || inputValue === '') {
      setlookbackDays(inputValue);
    }
  }

  function handleIntervalMinutesChange(e) {
    const inputValue = e.target.value;
    if (/^(\d+\.?\d*|\.\d+)$/.test(inputValue) || inputValue === '') {
      setintervalMinutes(inputValue);
    }
  }

  function update(e){
    e.preventDefault()
    handleSubmit(lookbackDays, intervalMinutes)
  }




    return  (
      <div className="darkBG">
      <div className="centered">

      <div className='modal' ref={chartRef}>
        <div className="modalHeader">
          <h5 className="heading">{machineName}</h5>
        </div>
        
        <LineChart width={900} height={600} data={data}>
            <Line type="monotone" dataKey="avg_interval_cycle_time" stroke="#2196F3" strokeWidth={2}/>
            <CartesianGrid stroke="#ccc" />
            <XAxis dataKey="newest_interval_timestamp" tickFormatter={(tickItem) => {
                const date = new Date(tickItem);
                const day = date.getDate().toString().padStart(2, '0');
                const month = (date.getMonth() + 1).toString().padStart(2, '0'); // Months are 0-based
                const year = date.getFullYear();
                const hours = date.getHours().toString().padStart(2, '0');
                const minutes = date.getMinutes().toString().padStart(2, '0');
                return `${day}.${month}.${year} ${hours}:${minutes}`
                //return date.toLocaleString(); // or any other format
              }}/>
            <YAxis />
            <Tooltip />
        </LineChart>
        <form onSubmit={update}>
          <div>
          <label>Kuvatavate päevade arv:</label>
          <input name="lookbackDays" type="text" placeholder="Päeva" onChange={handleLookbackDayChange} value={lookbackDays} className='input-field' />
          </div>
          <div>
          <label>Ümardatava intervalli pikkus minutites:</label>
          <input name="intervalMinutes" type="text" placeholder="Minutit" onChange={handleIntervalMinutesChange} value={intervalMinutes} className='input-field' />
          </div>
          <button className='updateBtn' >Update</button>
        </form>
      </div>
      </div>
      </div>
  )
}
