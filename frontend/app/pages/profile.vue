<template>
  <div class="profile-container">
    <div v-if="!user" class="loading-container">
      <LoadingSpinner text="Загрузка профиля..." />
    </div>
    
    <div v-else class="profile-card">
      <div class="profile-header">
        <div class="avatar">
          <span class="avatar-text">{{ userInitials }}</span>
        </div>
        <h1 class="profile-title">Профиль пользователя</h1>
      </div>
      
      <div class="profile-info">
        <div class="info-item">
          <label>Email:</label>
          <span class="email">{{ user.email }}</span>
          <span v-if="user.is_verified" class="verified-badge">✓ Подтвержден</span>
          <span v-else class="unverified-badge">⚠ Не подтвержден</span>
        </div>
        
        <div class="info-item">
          <label>Статус:</label>
          <span v-if="user.is_verified" class="status-verified">Активный</span>
          <span v-else class="status-unverified">Требует подтверждения</span>
        </div>
      </div>
      
      <div class="profile-actions">
        <button 
          v-if="!user.is_verified" 
          @click="resendVerification" 
          :disabled="isLoading"
          class="resend-button"
        >
          <span v-if="isLoading" class="loading-spinner"></span>
          {{ isLoading ? 'Отправка...' : 'Подтвердить email' }}
        </button>
        
        <div v-if="message" :class="['message', messageType]">
          {{ message }}
        </div>
        
        <LogoutButton />
      </div>

      <!-- Блок с доступными продуктами -->
      <div class="products-section">
        <h2 class="products-title">Доступные продукты</h2>
        <div class="products-grid">
          <div class="product-card">
            <div class="product-icon">📊</div>
            <h3 class="product-name">Аналитика</h3>
            <p class="product-description">
              Мощные инструменты для анализа данных и создания отчетов
            </p>
            <div class="product-actions">
              <button @click="goToProduct('analytics')" class="product-btn primary">
                Открыть
              </button>
              <button @click="startDemo('analytics')" class="product-btn demo">
                Демо
              </button>
            </div>
          </div>

          <div class="product-card">
            <div class="product-icon">🎯</div>
            <h3 class="product-name">Цели и задачи</h3>
            <p class="product-description">
              Планируйте цели, отслеживайте прогресс и достигайте результатов
            </p>
            <div class="product-actions">
              <button @click="goToProduct('goals')" class="product-btn primary">
                Открыть
              </button>
              <button @click="startDemo('goals')" class="product-btn demo">
                Демо
              </button>
            </div>
          </div>

          <div class="product-card">
            <div class="product-icon">📚</div>
            <h3 class="product-name">Обучение</h3>
            <p class="product-description">
              Интерактивные курсы и материалы для развития навыков
            </p>
            <div class="product-actions">
              <button @click="goToProduct('learning')" class="product-btn primary">
                Открыть
              </button>
              <button @click="startDemo('learning')" class="product-btn demo">
                Демо
              </button>
            </div>
          </div>

          <div class="product-card">
            <div class="product-icon">💬</div>
            <h3 class="product-name">Сообщество</h3>
            <p class="product-description">
              Общайтесь с единомышленниками и делитесь опытом
            </p>
            <div class="product-actions">
              <button @click="goToProduct('community')" class="product-btn primary">
                Открыть
              </button>
              <button @click="startDemo('community')" class="product-btn demo">
                Демо
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAuth } from '~/composables/useAuth'
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

const { user, getAuthHeaders } = useAuth()
const isLoading = ref(false)
const message = ref('')
const messageType = ref('')

// Вычисляем инициалы пользователя для аватара
const userInitials = computed(() => {
  if (!user.value?.email) return 'U'
  return user.value.email.charAt(0).toUpperCase()
})

// Функция для отправки запроса на повторную верификацию
const resendVerification = async () => {
  if (!user.value?.email) {
    showMessage('Ошибка: email не найден', 'error')
    return
  }
  
  isLoading.value = true
  message.value = ''
  
  try {
    const config = useRuntimeConfig()
    const apiBase = config.public.apiBase || 'http://localhost:8000'
    const response = await $fetch('/resend-verification', {
      method: 'POST',
      baseURL: apiBase,
      headers: {
        'Content-Type': 'application/json',
        ...getAuthHeaders()
      },
      body: {
        email: user.value.email
      }
    })
    
    if (response.success) {
      showMessage(response.message, 'success')
    } else {
      showMessage(response.message, 'warning')
    }
  } catch (error) {
    console.error('Ошибка при отправке верификации:', error)
    
    // Обрабатываем различные типы ошибок
    if (error.status === 404) {
      showMessage('Пользователь не найден', 'error')
    } else if (error.status === 500) {
      showMessage('Ошибка сервера. Попробуйте позже.', 'error')
    } else if (error.status === 0 || error.status === 'NETWORK_ERROR') {
      showMessage('Ошибка сети. Проверьте подключение к интернету.', 'error')
    } else {
      showMessage(error.data?.detail || 'Ошибка при отправке email. Попробуйте позже.', 'error')
    }
  } finally {
    isLoading.value = false
  }
}

// Функция для отображения сообщений
const showMessage = (text, type) => {
  message.value = text
  messageType.value = type
  
  // Автоматически скрываем сообщение через 5 секунд
  setTimeout(() => {
    message.value = ''
    messageType.value = ''
  }, 5000)
}

// Функция для перехода к продукту
const goToProduct = (productName) => {
  const router = useRouter()
  
  // Здесь можно добавить логику для перехода на соответствующие страницы
  // Пока что показываем сообщение
  showMessage(`Переход к продукту: ${productName}`, 'success')
  
  // Пример перехода (раскомментировать когда создадите страницы):
  // router.push(`/${productName}`)
}

// Функция для запуска демо
const startDemo = (productName) => {
  showMessage(`Запуск демо для продукта: ${productName}`, 'success')
  
  // Здесь можно добавить логику для запуска демо
  // Например, открытие модального окна с демо-версией
  console.log(`Демо запущено для: ${productName}`)
}

definePageMeta({
  middleware: 'auth'
})
</script>

<style scoped>
.profile-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.profile-card {
  background: white;
  border-radius: 20px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
  padding: 40px;
  max-width: 500px;
  width: 100%;
  text-align: center;
}

.profile-header {
  margin-bottom: 30px;
}

.avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 20px;
}

.avatar-text {
  color: white;
  font-size: 32px;
  font-weight: bold;
}

.profile-title {
  color: #333;
  font-size: 28px;
  font-weight: 600;
  margin: 0;
}

.profile-info {
  margin-bottom: 30px;
}

.info-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 15px 0;
  border-bottom: 1px solid #f0f0f0;
}

.info-item:last-child {
  border-bottom: none;
}

.info-item label {
  font-weight: 600;
  color: #666;
  min-width: 80px;
  text-align: left;
}

.email {
  color: #333;
  font-weight: 500;
  flex: 1;
  text-align: center;
}

.verified-badge {
  background: #10b981;
  color: white;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  margin-left: 10px;
}

.unverified-badge {
  background: #f59e0b;
  color: white;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  margin-left: 10px;
}

.status-verified {
  color: #10b981;
  font-weight: 600;
}

.status-unverified {
  color: #f59e0b;
  font-weight: 600;
}

.profile-actions {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.resend-button {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 15px 30px;
  border-radius: 10px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
}

.resend-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
}

.resend-button:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.loading-spinner {
  width: 20px;
  height: 20px;
  border: 2px solid transparent;
  border-top: 2px solid white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}



.message {
  padding: 12px 20px;
  border-radius: 8px;
  font-weight: 500;
  text-align: center;
}

.message.success {
  background: #d1fae5;
  color: #065f46;
  border: 1px solid #a7f3d0;
}

.message.error {
  background: #fee2e2;
  color: #991b1b;
  border: 1px solid #fca5a5;
}

.message.warning {
  background: #fef3c7;
  color: #92400e;
  border: 1px solid #fcd34d;
}

.loading-container {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 50vh;
}

/* Стили для блока с продуктами */
.products-section {
  margin-top: 40px;
  padding-top: 30px;
  border-top: 1px solid #f0f0f0;
}

.products-title {
  color: #333;
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 25px;
  text-align: center;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.product-card {
  background: #f8fafc;
  border-radius: 15px;
  padding: 25px;
  border: 1px solid #e2e8f0;
  transition: all 0.3s ease;
  text-align: center;
}

.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  border-color: #667eea;
}

.product-icon {
  font-size: 48px;
  margin-bottom: 15px;
}

.product-name {
  color: #333;
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 10px;
}

.product-description {
  color: #666;
  font-size: 14px;
  line-height: 1.5;
  margin-bottom: 20px;
  min-height: 60px;
}

.product-actions {
  display: flex;
  gap: 10px;
  justify-content: center;
}

.product-btn {
  padding: 10px 20px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
  min-width: 80px;
}

.product-btn.primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.product-btn.primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
}

.product-btn.demo {
  background: white;
  color: #667eea;
  border: 2px solid #667eea;
}

.product-btn.demo:hover {
  background: #667eea;
  color: white;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
}

@media (max-width: 600px) {
  .profile-card {
    padding: 30px 20px;
  }
  
  .profile-title {
    font-size: 24px;
  }
  
  .info-item {
    flex-direction: column;
    align-items: flex-start;
    gap: 5px;
  }
  
  .email {
    text-align: left;
  }
  
  .products-grid {
    grid-template-columns: 1fr;
    gap: 15px;
  }
  
  .product-card {
    padding: 20px;
  }
  
  .product-actions {
    flex-direction: column;
    gap: 8px;
  }
  
  .product-btn {
    width: 100%;
  }
}
</style>