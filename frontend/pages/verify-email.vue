<template>
  <div class="verify-email-container">
    <div class="verify-card">
      <h1>Верификация Email</h1>
      
      <div v-if="loading" class="loading">
        <p>Проверяем токен верификации...</p>
      </div>
      
      <div v-else-if="success" class="success">
        <div class="success-icon">✓</div>
        <h2>Email успешно верифицирован!</h2>
        <p>Теперь вы можете войти в свой аккаунт.</p>
        <nuxt-link to="/login" class="login-button">
          Перейти к входу
        </nuxt-link>
      </div>
      
      <div v-else-if="error" class="error">
        <div class="error-icon">✗</div>
        <h2>Ошибка верификации</h2>
        <p>{{ error }}</p>
        <div class="actions">
          <button @click="resendVerification" class="resend-button">
            Отправить новый email
          </button>
          <nuxt-link to="/login" class="login-link">
            Вернуться к входу
          </nuxt-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useRuntimeConfig } from 'nuxt/app'

const route = useRoute()
const router = useRouter()
const config = useRuntimeConfig()

const loading = ref(true)
const success = ref(false)
const error = ref(null)

const verifyEmail = async (token) => {
  try {
    const response = await $fetch(`/verify-email/${token}`, {
      method: 'GET',
      baseURL: config.public.apiBase,
    })
    
    if (response.success) {
      success.value = true
    } else {
      error.value = response.message || 'Неизвестная ошибка'
    }
  } catch (err) {
    console.error('Verification error:', err)
    error.value = err.data?.detail || err.message || 'Ошибка верификации email'
  } finally {
    loading.value = false
  }
}

const resendVerification = async () => {
  // Здесь можно добавить логику для повторной отправки email
  // Пока просто перенаправляем на страницу входа
  router.push('/login')
}

onMounted(() => {
  const token = route.query.token
  
  if (!token) {
    error.value = 'Токен верификации не найден'
    loading.value = false
    return
  }
  
  verifyEmail(token)
})
</script>

<style scoped>
.verify-email-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f5f5f5;
}

.verify-card {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  text-align: center;
  max-width: 400px;
  width: 100%;
}

.loading {
  color: #666;
}

.success {
  color: #2e7d32;
}

.success-icon {
  font-size: 3rem;
  color: #4caf50;
  margin-bottom: 1rem;
}

.error {
  color: #d32f2f;
}

.error-icon {
  font-size: 3rem;
  color: #f44336;
  margin-bottom: 1rem;
}

.login-button {
  display: inline-block;
  background-color: #4caf50;
  color: white;
  padding: 12px 24px;
  text-decoration: none;
  border-radius: 4px;
  margin-top: 1rem;
  transition: background-color 0.3s;
}

.login-button:hover {
  background-color: #45a049;
}

.actions {
  margin-top: 1rem;
}

.resend-button {
  background-color: #2196f3;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  margin-right: 1rem;
  transition: background-color 0.3s;
}

.resend-button:hover {
  background-color: #1976d2;
}

.login-link {
  color: #2196f3;
  text-decoration: none;
}

.login-link:hover {
  text-decoration: underline;
}
</style> 