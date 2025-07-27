export default defineNuxtRouteMiddleware(async (to, from) => {
  const { isAuthenticated, user, refreshUserData } = useAuth()
  
  // Проверяем, есть ли токен в localStorage
  if (process.client) {
    const token = localStorage.getItem('token')
    
    if (token && !isAuthenticated.value) {
      // Если есть токен, но состояние не инициализировано, загружаем данные пользователя
      try {
        await refreshUserData()
      } catch (error) {
        console.error('Middleware: Error loading user data:', error)
        // Если не удалось загрузить данные, перенаправляем на логин
        return navigateTo('/login')
      }
    }
  }
  
  // Проверяем авторизацию после попытки загрузки данных
  if (!isAuthenticated.value) {
    console.log('Middleware: User not authenticated, redirecting to login')
    return navigateTo('/login')
  }
  
  console.log('Middleware: User authenticated, proceeding to:', to.path)
})