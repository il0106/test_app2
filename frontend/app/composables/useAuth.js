import { ref, computed } from 'vue'

// Создаем реактивное состояние
const user = ref(null)
const token = ref(null)
const isAuthenticated = ref(false)
const isLoading = ref(false)

// Функция для загрузки данных пользователя
const loadUserData = async () => {
  if (!token.value) return null
  
  try {
    const config = useRuntimeConfig()
    const apiBase = config.public.apiBase || 'http://localhost:8000'
    
    const userData = await $fetch('/users/me', {
      baseURL: apiBase,
      headers: {
        'Authorization': `Bearer ${token.value}`
      }
    })
    
    user.value = userData
    isAuthenticated.value = true
    return userData
  } catch (error) {
    console.error('Ошибка загрузки данных пользователя:', error)
    // Если токен недействителен, очищаем состояние
    if (error.status === 401) {
      clearUser()
    }
    return null
  }
}

// Инициализируем токен из localStorage при загрузке
if (process.client) {
  const savedToken = localStorage.getItem('token')
  if (savedToken) {
    token.value = savedToken
    isAuthenticated.value = true
    // Загружаем данные пользователя асинхронно
    loadUserData()
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
      // Загружаем данные пользователя после установки токена
      loadUserData()
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

  // Функция для принудительной загрузки данных пользователя
  const refreshUserData = async () => {
    if (isLoading.value) return user.value
    
    isLoading.value = true
    try {
      const userData = await loadUserData()
      return userData
    } finally {
      isLoading.value = false
    }
  }

  return {
    user: computed(() => user.value),
    token: computed(() => token.value),
    isAuthenticated: computed(() => isAuthenticated.value),
    isLoading: computed(() => isLoading.value),
    setUser,
    setToken,
    clearUser,
    getAuthHeaders,
    refreshUserData
  }
} 