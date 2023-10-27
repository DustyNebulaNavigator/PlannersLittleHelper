import { useEffect, useState } from 'react'
import {Route, Routes} from 'react-router-dom'
import './App.css'


import Navbar from './components/navbar/Navbar'
import CycleTimesPage from './components/MI/CycleTimesPage'
import Home from './components/Home/index'
import GetPartById from './components/Monitor/GetPartById'
import MachineCycleTimeModal from './components/MI/MachineCycleTimeModal'

function App() {
  return (
    <>
    <Navbar />
    <div className='container'>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/cycletimes" element={<CycleTimesPage />} />
        <Route path="/getPartDescription" element={<GetPartById />} />
        <Route path="/macinecyclestats" element={<MachineCycleTimeModal />} />
      </Routes>
    
    </div>
    </>
  )
}

export default App
