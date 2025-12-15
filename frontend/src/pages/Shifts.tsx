import React, { useEffect, useState } from 'react'
import axios from 'axios'

export default function Shifts(){
  const [timesheet, setTimesheet] = useState<any[]>([])
  const token = localStorage.getItem('token')

  useEffect(()=>{
    fetchTimesheet()
  },[])

  async function fetchTimesheet(){
    try {
      const res = await axios.get('http://localhost:8000/shifts/timesheet', {headers: {Authorization: `Bearer ${token}`}})
      setTimesheet(res.data)
    } catch(e) {
      console.error(e)
    }
  }

  async function checkIn(){
    try {
      await axios.post('http://localhost:8000/shifts/checkin', {}, {headers: {Authorization: `Bearer ${token}`}})
      fetchTimesheet()
    } catch(e) {
      console.error(e)
    }
  }

  async function checkOut(){
    try {
      await axios.post('http://localhost:8000/shifts/checkout', {}, {headers: {Authorization: `Bearer ${token}`}})
      fetchTimesheet()
    } catch(e) {
      console.error(e)
    }
  }

  return (
    <div className="page">
      <h2>Shifts & Time Tracking</h2>
      <div className="actions">
        <button onClick={checkIn}>Check In</button>
        <button onClick={checkOut}>Check Out</button>
      </div>
      <table className="table">
        <thead>
          <tr><th>Date</th><th>Check In</th><th>Check Out</th></tr>
        </thead>
        <tbody>
          {timesheet.map(t=> (
            <tr key={t.id}><td>{t.date}</td><td>{t.check_in_time?.substring(0,19)}</td><td>{t.check_out_time?.substring(0,19)}</td></tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}