import { useEffect, useState } from 'react'
import {Route, Routes} from 'react-router-dom'
import './App.css'


import Navbar from './components/navbar/Navbar'
import CycleTimesPage from './components/MI/CycleTimesPage'
import Home from './components/Home/index'
import GetPartById from './components/Monitor/GetPartById'

function App() {
  return (
    <>
    <Navbar />
    <div className='container'>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/cycletimes" element={<CycleTimesPage />} />
        <Route path="/getPartDescription" element={<GetPartById />} />
      </Routes>
    
    </div>
    </>
  )
}

export default App
