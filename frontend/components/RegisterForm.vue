<template>
    <form @submit.prevent="register">
      <div>
        <label for="email">Email</label>
        <input id="email" v-model="email" type="email" required />
      </div>
      <div>
        <label for="password">Password</label>
        <input id="password" v-model="password" type="password" required />
      </div>
      <button type="submit">Register</button>
      <p v-if="error" class="error">{{ error }}</p>
    </form>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import { useRuntimeConfig } from 'nuxt/app'
  import { useAuth } from '~/composables/useAuth'
  
  const router = useRouter()
  const config = useRuntimeConfig()
  const { setToken, setUser } = useAuth()
  
  const email = ref('')
  const password = ref('')
  const error = ref(null)
  
  const register = async () => {
    error.value = null
    try {
      const response = await $fetch('/auth/register', {
        method: 'POST',
        body: {
          email: email.value,
          password: password.value,
        },
        baseURL: config.public.apiBase,
      })
      
      // После успешной регистрации можно автоматически войти
      const loginResponse = await $fetch('/auth/jwt/login', {
        method: 'POST',
        body: new URLSearchParams({
          username: email.value,
          password: password.value,
        }),
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        baseURL: config.public.apiBase,
      })
      
      // Сохраняем токен
      if (loginResponse.access_token) {
        setToken(loginResponse.access_token)
      }
      
      // Получаем информацию о пользователе
      const user = await $fetch('/users/me', {
        baseURL: config.public.apiBase,
        headers: {
          'Authorization': `Bearer ${loginResponse.access_token}`
        }
      })
      
      // Store user data
      setUser(user)
      
      // Перенаправляем на защищенную страницу
      router.push('/profile')
    } catch (err) {
      error.value = err.data?.detail || err.message
    }
  }
  </script>
  
  <style scoped>
  .error {
    color: red;
  }
  </style>