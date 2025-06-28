import { ref, computed } from 'vue'

// Создаем реактивное состояние
const user = ref(null)
const token = ref(null)
const isAuthenticated = ref(false)

// Инициализируем токен из localStorage при загрузке
if (process.client) {
  const savedToken = localStorage.getItem('token')
  if (savedToken) {
    token.value = savedToken
    isAuthenticated.value = true
  }
}

export const useAuth = () => {
  const setUser = (userData) => {
    user.value = userData
    isAuthenticated.value = !!userData
  }

  const setToken = (newToken) => {
    console.log('Setting token:', newToken ? 'token received' : 'no token')
    token.value = newToken
    if (newToken) {
      localStorage.setItem('token', newToken)
      isAuthenticated.value = true
      console.log('Token saved to localStorage and state updated')
    } else {
      localStorage.removeItem('token')
      isAuthenticated.value = false
      console.log('Token removed from localStorage and state updated')
    }
  }

  const clearUser = () => {
    user.value = null
    token.value = null
    isAuthenticated.value = false
    localStorage.removeItem('token')
  }

  const getAuthHeaders = () => {
    return token.value ? { 'Authorization': `Bearer ${token.value}` } : {}
  }

  return {
    user: computed(() => user.value),
    token: computed(() => token.value),
    isAuthenticated: computed(() => isAuthenticated.value),
    setUser,
    setToken,
    clearUser,
    getAuthHeaders
  }
} 