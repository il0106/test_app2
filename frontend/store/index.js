export const state = () => ({
    user: null,
    isAuthenticated: false,
    token: null,
  })
  
  export const mutations = {
    setUser(state, user) {
      state.user = user
      state.isAuthenticated = !!user
    },
    clearUser(state) {
      state.user = null
      state.isAuthenticated = false
      state.token = null
    },
    setToken(state, token) {
      state.token = token
      if (token) {
        localStorage.setItem('token', token)
      } else {
        localStorage.removeItem('token')
      }
    },
  }
  
  export const actions = {
    nuxtClientInit({ commit }) {
      // Восстанавливаем токен из localStorage при загрузке клиента
      const token = localStorage.getItem('token')
      if (token) {
        commit('setToken', token)
        // Можно также попробовать получить информацию о пользователе
        // но это лучше делать в компонентах, где есть доступ к $fetch
      }
    }
  }
  
  // Note: nuxtServerInit is not available in Nuxt 3
  // You can use plugins or middleware for authentication checks