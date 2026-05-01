"use client"
import {useState, useEffect} from "react"
import axios from "axios"


export default function Home() {
  
  const [ollamaModels, setOllamaModels] = useState<string[]>([])
  const [error, setError] = useState<string | null>(null)
  
  useEffect(() => {
    axios.get("http://localhost:8001/api/v1/models").then((reponse) => {
      setOllamaModels(reponse.data.models)
    }).catch((err) => {
      setError(err.message)
    })
  }, [])
  
  if(error) return <div>Error: {error}</div>
  
  return (
    <div>
      <h1>Ollama Models</h1>
      <ul>
        {ollamaModels.map((model) => (
            <li key={model}>{model}</li>
        ))}
      </ul>
    </div>
  )
}
