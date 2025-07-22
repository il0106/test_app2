<template>
  <div class="landing-page">
    <!-- Header с логотипом и кнопками авторизации -->
    <header class="header">
      <div class="logo">
        <img src="~assets/public/img/logo-no-background.svg" alt="Logo" class="logo-img">
      </div>
      
      <div class="auth-buttons">
        <button @click="goToLogin" class="auth-btn login-btn">Войти</button>
        <button @click="goToRegister" class="auth-btn register-btn">Регистрация</button>
      </div>
    </header>

    <!-- Основной контент лендинга -->
    <main class="main-content">
      <!-- Hero секция -->
      <section class="hero-section">
        <div class="hero-content">
          <h1 class="hero-title">Добро пожаловать</h1>
          <p class="hero-subtitle">Создавайте, развивайтесь и достигайте новых высот</p>
          <button class="cta-button">Начать</button>
        </div>
      </section>

      <!-- О нас секция -->
      <section class="about-section">
        <div class="container">
          <h2 class="section-title">О нас</h2>
          <p class="section-text">
            Мы помогаем людям развивать свои навыки и достигать поставленных целей. 
            Наша платформа предоставляет все необходимые инструменты для успешного обучения.
          </p>
        </div>
      </section>

      <!-- Преимущества секция -->
      <section class="features-section">
        <div class="container">
          <h2 class="section-title">Наши преимущества</h2>
          <div class="features-grid">
            <div class="feature-card">
              <div class="feature-icon">🚀</div>
              <h3>Быстрый старт</h3>
              <p>Начните обучение уже сегодня с нашими простыми и понятными материалами</p>
            </div>
            <div class="feature-card">
              <div class="feature-icon">📚</div>
              <h3>Качественные материалы</h3>
              <p>Только проверенный контент от экспертов в своих областях</p>
            </div>
            <div class="feature-card">
              <div class="feature-icon">👥</div>
              <h3>Сообщество</h3>
              <p>Присоединяйтесь к сообществу единомышленников и развивайтесь вместе</p>
            </div>
          </div>
        </div>
      </section>

      <!-- Контакты секция -->
      <section class="contact-section">
        <div class="container">
          <h2 class="section-title">Свяжитесь с нами</h2>
          <p class="section-text">
            Есть вопросы? Мы всегда готовы помочь и ответить на все ваши вопросы.
          </p>
          <button class="contact-button">Написать нам</button>
        </div>
      </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
      <div class="container">
        <p>&copy; 2024 Все права защищены</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
const router = useRouter();

const goToLogin = () => {
  router.push('/login');
};

const goToRegister = () => {
  router.push('/register');
};
</script>

<style scoped>
.landing-page {
  min-height: 100vh;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  line-height: 1.6;
  color: #333;
}

/* Header */
.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
  z-index: 1000;
}

.logo-img {
  height: 40px;
  width: auto;
}

.auth-buttons {
  display: flex;
  gap: 1rem;
}

.auth-btn {
  padding: 0.5rem 1.5rem;
  border: none;
  border-radius: 6px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  font-size: 0.9rem;
}

.login-btn {
  background: transparent;
  color: #333;
  border: 1px solid #ddd;
}

.login-btn:hover {
  background: #f5f5f5;
  border-color: #ccc;
}

.register-btn {
  background: #007bff;
  color: white;
}

.register-btn:hover {
  background: #0056b3;
}

/* Main Content */
.main-content {
  padding-top: 80px;
}

/* Hero Section */
.hero-section {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  text-align: center;
  padding: 2rem;
}

.hero-content {
  max-width: 800px;
}

.hero-title {
  font-size: 3.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
  line-height: 1.2;
}

.hero-subtitle {
  font-size: 1.25rem;
  margin-bottom: 2rem;
  opacity: 0.9;
}

.cta-button {
  padding: 1rem 2rem;
  font-size: 1.1rem;
  background: white;
  color: #667eea;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.cta-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
}

/* Sections */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 2rem;
  color: #333;
}

.section-text {
  font-size: 1.1rem;
  text-align: center;
  max-width: 600px;
  margin: 0 auto 2rem;
  color: #666;
}

/* About Section */
.about-section {
  padding: 5rem 0;
  background: #f8f9fa;
}

/* Features Section */
.features-section {
  padding: 5rem 0;
  background: white;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-top: 3rem;
}

.feature-card {
  text-align: center;
  padding: 2rem;
  border-radius: 12px;
  background: #f8f9fa;
  transition: transform 0.2s ease;
}

.feature-card:hover {
  transform: translateY(-5px);
}

.feature-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.feature-card h3 {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: #333;
}

.feature-card p {
  color: #666;
  line-height: 1.6;
}

/* Contact Section */
.contact-section {
  padding: 5rem 0;
  background: #f8f9fa;
  text-align: center;
}

.contact-button {
  padding: 1rem 2rem;
  font-size: 1.1rem;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.contact-button:hover {
  background: #0056b3;
  transform: translateY(-2px);
}

/* Footer */
.footer {
  padding: 2rem 0;
  background: #333;
  color: white;
  text-align: center;
}

/* Responsive Design */
@media (max-width: 768px) {
  .header {
    padding: 1rem;
  }
  
  .hero-title {
    font-size: 2.5rem;
  }
  
  .hero-subtitle {
    font-size: 1.1rem;
  }
  
  .section-title {
    font-size: 2rem;
  }
  
  .features-grid {
    grid-template-columns: 1fr;
  }
  
  .auth-buttons {
    gap: 0.5rem;
  }
  
  .auth-btn {
    padding: 0.4rem 1rem;
    font-size: 0.8rem;
  }
}

@media (max-width: 480px) {
  .hero-title {
    font-size: 2rem;
  }
  
  .container {
    padding: 0 1rem;
  }
  
  .logo-img {
    height: 30px;
  }
}
</style>