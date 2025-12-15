import React, { useEffect, useState } from 'react'
import { BrowserRouter, Routes, Route, Link, useNavigate } from 'react-router-dom'
import Login from './pages/Login'
import Dashboard from './pages/Dashboard'
import Messages from './pages/Messages'
import Keywords from './pages/Keywords'
import Users from './pages/Users'
import Reports from './pages/Reports'
import Requests from './pages/Requests'
import Shifts from './pages/Shifts'
import KPI from './pages/KPI'
import './App.css'

export default function App(){
  const [loggedIn, setLoggedIn] = useState(false)
  const [user, setUser] = useState<any>(null)
  const nav = useNavigate()

  useEffect(() => {
    const token = localStorage.getItem('token')
    if(token) setLoggedIn(true)
  }, [])

  const handleLogout = () => {
    localStorage.removeItem('token')
    setLoggedIn(false)
    nav('/')
  }

  if(!loggedIn) {
    return <Login onLogin={() => setLoggedIn(true)} />
  }

  return (
    <div className="app-container">
      <nav className="navbar">
        <h1>OmniChat</h1>
        <ul>
          <li><Link to="/dashboard">Dashboard</Link></li>
          <li><Link to="/messages">Messages</Link></li>
          <li><Link to="/keywords">Keywords</Link></li>
          <li><Link to="/users">Users</Link></li>
          <li><Link to="/reports">Reports</Link></li>
          <li><Link to="/requests">Requests</Link></li>
          <li><Link to="/shifts">Shifts</Link></li>
          <li><Link to="/kpi">KPI</Link></li>
          <li><button onClick={handleLogout}>Logout</button></li>
        </ul>
      </nav>
      
      <Routes>
        <Route path="/dashboard" element={<Dashboard/>} />
        <Route path="/messages" element={<Messages/>} />
        <Route path="/keywords" element={<Keywords/>} />
        <Route path="/users" element={<Users/>} />
        <Route path="/reports" element={<Reports/>} />
        <Route path="/requests" element={<Requests/>} />
        <Route path="/shifts" element={<Shifts/>} />
        <Route path="/kpi" element={<KPI/>} />
        <Route path="/" element={<Dashboard/>} />
      </Routes>
    </div>
  )
}
