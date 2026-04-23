import axios from 'axios'

export const api = axios.create({
  baseURL: '/api/v1',
  timeout: 15000,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    const message = error.response?.data?.detail || error.message || 'Unknown error'
    console.error(`[API Error] ${error.config?.url}: ${message}`)
    return Promise.reject(error)
  }
)
