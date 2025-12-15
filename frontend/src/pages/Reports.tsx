import React, { useEffect, useState } from 'react'
import axios from 'axios'

export default function Reports(){
  const [report, setReport] = useState<any>(null)
  const [groupBy, setGroupBy] = useState('department')
  const token = localStorage.getItem('token')

  useEffect(()=>{
    fetchReport()
  },[groupBy])

  async function fetchReport(){
    try {
      const res = await axios.get(`http://localhost:8000/reports/summary?group_by=${groupBy}`, {headers: {Authorization: `Bearer ${token}`}})
      setReport(res.data)
    } catch(e) {
      console.error(e)
    }
  }

  return (
    <div className="page">
      <h2>Reports</h2>
      <div className="form-group">
        <label>Group By:</label>
        <select value={groupBy} onChange={e=>setGroupBy(e.target.value)}>
          <option value="department">Department</option>
          <option value="user">User</option>
          <option value="total">Total</option>
        </select>
      </div>
      {report && (
        <div>
          <h3>Summary</h3>
          <p>Total Messages: {report.count}</p>
          <p>Grouped By: {report.by}</p>
          <div className="report-buckets">
            {Object.entries(report.buckets || {}).map(([k, v]: [string, any]) => (
              <div key={k} className="bucket">
                <strong>{k}</strong>: {v}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}