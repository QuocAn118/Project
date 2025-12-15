import React, { useEffect, useState } from 'react'
import axios from 'axios'

export default function Keywords(){
  const [keywords, setKeywords] = useState<any[]>([])
  const [newWord, setNewWord] = useState('')
  const [depId, setDepId] = useState(1)
  const token = localStorage.getItem('token')

  useEffect(()=>{
    fetchKeywords()
  },[])

  async function fetchKeywords(){
    try {
      const res = await axios.get('http://localhost:8000/keywords', {headers: {Authorization: `Bearer ${token}`}})
      setKeywords(res.data)
    } catch(e) {
      console.error(e)
    }
  }

  async function addKeyword(){
    if(!newWord) return
    try {
      await axios.post('http://localhost:8000/keywords', {word: newWord, department_id: depId}, {headers: {Authorization: `Bearer ${token}`}})
      setNewWord('')
      fetchKeywords()
    } catch(e) {
      console.error(e)
    }
  }

  async function deleteKeyword(id: number){
    try {
      await axios.delete(`http://localhost:8000/keywords/${id}`, {headers: {Authorization: `Bearer ${token}`}})
      fetchKeywords()
    } catch(e) {
      console.error(e)
    }
  }

  return (
    <div className="page">
      <h2>Keywords</h2>
      <div className="form-group">
        <input type="text" placeholder="New keyword" value={newWord} onChange={e=>setNewWord(e.target.value)} />
        <input type="number" placeholder="Dept ID" value={depId} onChange={e=>setDepId(parseInt(e.target.value))} />
        <button onClick={addKeyword}>Add</button>
      </div>
      <table className="table">
        <thead>
          <tr><th>ID</th><th>Word</th><th>Dept ID</th><th>Action</th></tr>
        </thead>
        <tbody>
          {keywords.map(k=> (
            <tr key={k.id}><td>{k.id}</td><td>{k.word}</td><td>{k.department_id}</td><td><button onClick={()=>deleteKeyword(k.id)}>Delete</button></td></tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}