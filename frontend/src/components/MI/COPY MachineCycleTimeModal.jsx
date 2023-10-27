import { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';
import {CartesianGrid, Legend, Line, LineChart, Tooltip, XAxis, YAxis} from "recharts";

import './MachineCycleTimeModal.css'

export default function MachineCycleTimeModal ({machineName}){
    
    const [data, setData] = useState([])

    const location = useLocation();
    const queryParams = new URLSearchParams(location.search);

    
    //const machineName = queryParams.get('machine_name');
    //let lookbackDays = queryParams.get('lookback_days');
    //let intervalMinutes = queryParams.get('interval_minutes');
    
    let lookbackDays=1
    let intervalMinutes=20

    useEffect((machineName)=>{
        async function getchAverageCycletimes(){
            try {
                const response = await fetch(`${import.meta.env.VITE_API_URL}macinecyclestats/?machine_name=${machineName}&lookback_days=${lookbackDays}&interval_minutes=${intervalMinutes}`)
                console.log(`${import.meta.env.VITE_API_URL}macinecyclestats/?machine_name=${machineName}&lookback_days=${lookbackDays}&interval_minutes=${intervalMinutes}`)
                if (!response.ok) {
                  throw new Error('Network response not ok')
                }
                const result = await response.json();
                setData(result)
              } catch (error) {
                console.log('Error fetching data:', error)
              }
        }
        getchAverageCycletimes()
    },[])

    return  <div>
    <h1>{machineName}</h1>
    <LineChart width={900} height={600} data={data}>
        <Line type="monotone" dataKey="avg_interval_cycle_time" stroke="#2196F3" strokeWidth={2}/>
        <CartesianGrid stroke="#ccc" />
        <XAxis dataKey="newest_interval_timestamp" tickFormatter={(tickItem) => {
            const date = new Date(tickItem);
            return date.toLocaleString(); // or any other format
          }}/>
        <YAxis />
        <Tooltip />
        <Legend />
    </LineChart>
  </div>
}
