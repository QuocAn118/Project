import React, { useEffect, useState } from 'react'
import axios from 'axios'

type Msg = {
  id: number
  platform: string
  sender: string
  content: string
  keywords?: string
}

export default function Messages(){
  const [msgs,setMsgs] = useState<Msg[]>([])
  const token = localStorage.getItem('token')

  useEffect(()=>{
    fetchMessages()
  },[])

  async function fetchMessages(){
    try {
      const res = await axios.get('http://localhost:8000/messages', {headers: {Authorization: `Bearer ${token}`}})
      setMsgs(res.data)
    } catch(e) {
      console.error(e)
    }
  }

  async function complete(id: number){
    try {
      await axios.post(`http://localhost:8000/messages/${id}/complete`, {}, {headers:{Authorization:`Bearer ${token}`}})
      fetchMessages()
    } catch(e) {
      console.error(e)
    }
  }

  return (
    <div className="page">
      <h2>Messages</h2>
      <table className="table">
        <thead>
          <tr><th>ID</th><th>Platform</th><th>Sender</th><th>Content</th><th>Keywords</th><th>Action</th></tr>
        </thead>
        <tbody>
          {msgs.map(m=> (
            <tr key={m.id}><td>{m.id}</td><td>{m.platform}</td><td>{m.sender}</td><td>{m.content.substring(0,50)}</td><td>{m.keywords}</td><td><button onClick={()=>complete(m.id)}>Complete</button></td></tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}