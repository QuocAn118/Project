import React, { useEffect, useState } from 'react'
import axios from 'axios'

export default function KPI(){
  const [metrics, setMetrics] = useState<any[]>([])
  const token = localStorage.getItem('token')

  useEffect(()=>{
    fetchKPI()
  },[])

  async function fetchKPI(){
    try {
      const res = await axios.get('http://localhost:8000/kpi/user', {headers: {Authorization: `Bearer ${token}`}})
      setMetrics(res.data.metrics || [])
    } catch(e) {
      console.error(e)
    }
  }

  return (
    <div className="page">
      <h2>KPI Metrics</h2>
      <table className="table">
        <thead>
          <tr><th>Metric</th><th>Value</th><th>Period</th></tr>
        </thead>
        <tbody>
          {metrics.map((m: any, i: number) => (
            <tr key={i}><td>{m.metric_name}</td><td>{m.metric_value}</td><td>{m.period}</td></tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}