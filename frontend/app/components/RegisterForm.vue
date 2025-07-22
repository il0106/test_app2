<template>
    <form @submit.prevent="register" class="auth-form">
      <div class="form-group">
        <label for="email">Email</label>
        <input 
          id="email" 
          v-model="email" 
          type="email" 
          required 
          :disabled="loading"
          class="form-input"
          placeholder="Введите ваш email"
        />
      </div>
      <div class="form-group">
        <label for="password">Пароль</label>
        <input 
          id="password" 
          v-model="password" 
          type="password" 
          required 
          :disabled="loading"
          class="form-input"
          placeholder="Введите пароль"
          minlength="6"
        />
      </div>
      <button 
        type="submit" 
        :disabled="loading || !email || !password"
        class="submit-button"
      >
        <span v-if="loading">Регистрация...</span>
        <span v-else>Зарегистрироваться</span>
      </button>
      <p v-if="error" class="error">{{ error }}</p>
      <p v-if="success" class="success">{{ success }}</p>
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
  const success = ref(null)
  const loading = ref(false)
  
  const register = async () => {
    error.value = null
    success.value = null
    loading.value = true
    
    try {
      console.log('Registering user:', email.value)
      
      const response = await $fetch('/auth/register', {
        method: 'POST',
        body: {
          email: email.value,
          password: password.value,
        },
        baseURL: config.public.apiBase,
      })
      
      console.log('Registration successful:', response)
      success.value = 'Регистрация успешна! Выполняется вход...'
      
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
      
      console.log('Login successful:', loginResponse)
      
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
      
      console.log('User data retrieved:', user)
      
      // Store user data
      setUser(user)
      
      // Перенаправляем на защищенную страницу
      router.push('/profile')
    } catch (err) {
      console.error('Registration error:', err)
      error.value = err.data?.detail || err.message || 'Ошибка регистрации'
    } finally {
      loading.value = false
    }
  }
  </script>
  
  <style scoped>
.auth-form {
  width: 100%;
}

.form-group {
  margin-bottom: 1.5rem;
  text-align: left;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
  color: #333;
}

.form-input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 1rem;
  transition: border-color 0.2s ease;
  box-sizing: border-box;
}

.form-input:focus {
  outline: none;
  border-color: #007bff;
  box-shadow: 0 0 0 2px rgba(0, 123, 255, 0.25);
}

.form-input:disabled {
  background-color: #f5f5f5;
  cursor: not-allowed;
}

.submit-button {
  width: 100%;
  padding: 0.75rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  margin-top: 1rem;
}

.submit-button:hover:not(:disabled) {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.submit-button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

.error {
  color: #dc3545;
  background-color: #f8d7da;
  border: 1px solid #f5c6cb;
  padding: 0.75rem;
  border-radius: 6px;
  margin-top: 1rem;
  font-size: 0.9rem;
}

.success {
  color: #155724;
  background-color: #d4edda;
  border: 1px solid #c3e6cb;
  padding: 0.75rem;
  border-radius: 6px;
  margin-top: 1rem;
  font-size: 0.9rem;
}
</style>