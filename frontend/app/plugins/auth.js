export default defineNuxtPlugin(async (nuxtApp) => {
  // Инициализируем авторизацию при загрузке приложения
  nuxtApp.hook('app:created', async () => {
    const { refreshUserData } = useAuth()
    
    // Проверяем, есть ли токен в localStorage
    if (process.client) {
      const token = localStorage.getItem('token')
      if (token) {
        console.log('Plugin: Found token in localStorage, loading user data...')
        try {
          await refreshUserData()
          console.log('Plugin: User data loaded successfully')
        } catch (error) {
          console.error('Plugin: Error loading user data:', error)
        }
      }
    }
  })

  // Добавляем токен к запросам автоматически
  nuxtApp.hook('app:created', () => {
    // Перехватываем все fetch запросы
    const originalFetch = globalThis.$fetch
    if (originalFetch) {
      globalThis.$fetch = async (request, options = {}) => {
        // Получаем токен из localStorage
        const token = localStorage.getItem('token')
        console.log('Plugin: Token from localStorage:', token ? 'token exists' : 'no token')
        
        if (token) {
          if (!options.headers) {
            options.headers = {}
          }
          options.headers['Authorization'] = `Bearer ${token}`
          console.log('Plugin: Added Authorization header to request:', request)
        }
        
        return originalFetch(request, options)
      }
    } else {
      console.log('Plugin: $fetch not found in globalThis')
    }
  })
}) 