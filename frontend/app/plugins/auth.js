export default defineNuxtPlugin((nuxtApp) => {
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