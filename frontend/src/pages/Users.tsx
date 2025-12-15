import React, { useEffect, useState } from 'react'
import axios from 'axios'

export default function Users(){
  const [users, setUsers] = useState<any[]>([])
  const token = localStorage.getItem('token')

  useEffect(()=>{
    fetchUsers()
  },[])

  async function fetchUsers(){
    try {
      const res = await axios.get('http://localhost:8000/users', {headers: {Authorization: `Bearer ${token}`}})
      setUsers(res.data)
    } catch(e) {
      console.error(e)
    }
  }

  return (
    <div className="page">
      <h2>Users</h2>
      <table className="table">
        <thead>
          <tr><th>ID</th><th>Username</th><th>Full Name</th><th>Role</th><th>KPI Score</th></tr>
        </thead>
        <tbody>
          {users.map(u=> (
            <tr key={u.id}><td>{u.id}</td><td>{u.username}</td><td>{u.full_name}</td><td>{u.role}</td><td>{u.kpi_score}</td></tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}