import React, { useEffect, useState } from 'react'
import axios from 'axios'

export default function Requests(){
  const [requests, setRequests] = useState<any[]>([])
  const [showForm, setShowForm] = useState(false)
  const [reqType, setReqType] = useState('leave')
  const [desc, setDesc] = useState('')
  const token = localStorage.getItem('token')

  useEffect(()=>{
    fetchRequests()
  },[])

  async function fetchRequests(){
    try {
      const res = await axios.get('http://localhost:8000/requests', {headers: {Authorization: `Bearer ${token}`}})
      setRequests(res.data)
    } catch(e) {
      console.error(e)
    }
  }

  async function submitRequest(){
    if(!desc) return
    try {
      await axios.post('http://localhost:8000/requests', {request_type: reqType, description: desc}, {headers: {Authorization: `Bearer ${token}`}})
      setDesc('')
      setShowForm(false)
      fetchRequests()
    } catch(e) {
      console.error(e)
    }
  }

  return (
    <div className="page">
      <h2>Requests</h2>
      <button onClick={() => setShowForm(!showForm)}>New Request</button>
      {showForm && (
        <div className="form-group">
          <select value={reqType} onChange={e=>setReqType(e.target.value)}>
            <option value="leave">Leave</option>
            <option value="raise">Raise</option>
          </select>
          <textarea placeholder="Description" value={desc} onChange={e=>setDesc(e.target.value)} />
          <button onClick={submitRequest}>Submit</button>
        </div>
      )}
      <table className="table">
        <thead>
          <tr><th>ID</th><th>Type</th><th>Description</th><th>Status</th><th>Submitted</th></tr>
        </thead>
        <tbody>
          {requests.map(r=> (
            <tr key={r.id}><td>{r.id}</td><td>{r.request_type}</td><td>{r.description.substring(0,50)}</td><td>{r.status}</td><td>{r.submitted_at}</td></tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}