import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'

export default function Login({onLogin}: any){
  const [username,setUsername] = useState('')
  const [password,setPassword] = useState('')
  const [error, setError] = useState('')
  const nav = useNavigate()

  const submit = async (e: any) =>{
    e.preventDefault()
    try {
      const form = new URLSearchParams()
      form.append('username', username)
      form.append('password', password)
      const res = await axios.post('http://localhost:8000/auth/token', form)
      localStorage.setItem('token', res.data.access_token)
      onLogin()
      nav('/dashboard')
    } catch(err) {
      setError('Login failed. Invalid credentials.')
    }
  }

  return (
    <div className="login-container">
      <form onSubmit={submit} className="login-form">
        <h2>OmniChat Login</h2>
        {error && <div className="error">{error}</div>}
        <div className="form-group">
          <label>Username</label>
          <input value={username} onChange={e=>setUsername(e.target.value)} required />
        </div>
        <div className="form-group">
          <label>Password</label>
          <input type="password" value={password} onChange={e=>setPassword(e.target.value)} required />
        </div>
        <button type="submit">Login</button>
        <p>Demo credentials: admin / adminpass, staff1 / staff1pass</p>
      </form>
    </div>
  )
}
