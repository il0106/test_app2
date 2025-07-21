<template>
  <div class="auth-page">
    <header class="auth-header">
      <button @click="goBack" class="back-button">
        ← Назад
      </button>
    </header>
    
    <div class="auth-container">
      <div class="auth-card">
        <div class="auth-logo">
          <img src="~assets/public/img/logo-no-background.svg" alt="Logo" class="logo-img">
        </div>
        
        <h1 class="auth-title">Вход в систему</h1>
        
        <LoginForm />
        
        <p class="auth-link">
          Нет аккаунта? <nuxt-link to="/register" class="link">Зарегистрироваться</nuxt-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import LoginForm from '@/components/LoginForm'

const router = useRouter();

const goBack = () => {
  router.push('/');
};
</script>

<style scoped>
.auth-page {
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  flex-direction: column;
}

.auth-header {
  padding: 1rem 2rem;
}

.back-button {
  background: rgba(255, 255, 255, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.3);
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  backdrop-filter: blur(10px);
}

.back-button:hover {
  background: rgba(255, 255, 255, 0.3);
}

.auth-container {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.auth-card {
  background: white;
  padding: 3rem;
  border-radius: 16px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
  text-align: center;
}

.auth-logo {
  margin-bottom: 2rem;
}

.logo-img {
  height: 50px;
  width: auto;
}

.auth-title {
  font-size: 2rem;
  font-weight: 700;
  color: #333;
  margin-bottom: 2rem;
}

.auth-link {
  margin-top: 2rem;
  color: #666;
}

.link {
  color: #007bff;
  text-decoration: none;
  font-weight: 500;
}

.link:hover {
  text-decoration: underline;
}

@media (max-width: 480px) {
  .auth-card {
    padding: 2rem;
    margin: 1rem;
  }
  
  .auth-title {
    font-size: 1.5rem;
  }
}
</style>