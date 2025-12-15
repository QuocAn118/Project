import React, { useEffect, useState } from 'react'
import axios from 'axios'

export default function Dashboard(){
  const [stats, setStats] = useState<any>({})
  const token = localStorage.getItem('token')

  useEffect(()=>{
    fetchStats()
  },[])

  async function fetchStats(){
    try {
      const msgRes = await axios.get('http://localhost:8000/messages', {headers: {Authorization: `Bearer ${token}`}})
      const reqRes = await axios.get('http://localhost:8000/requests', {headers: {Authorization: `Bearer ${token}`}})
      setStats({
        total_messages: msgRes.data.length,
        total_requests: reqRes.data.length,
        pending_requests: reqRes.data.filter((r:any) => r.status === 'pending').length
      })
    } catch(e) {
      console.error(e)
    }
  }

  return (
    <div className="page">
      <h2>Dashboard</h2>
      <div className="stats-grid">
        <div className="stat-card">
          <h3>Total Messages</h3>
          <p>{stats.total_messages || 0}</p>
        </div>
        <div className="stat-card">
          <h3>Total Requests</h3>
          <p>{stats.total_requests || 0}</p>
        </div>
        <div className="stat-card">
          <h3>Pending Requests</h3>
          <p>{stats.pending_requests || 0}</p>
        </div>
      </div>
    </div>
  )
}
