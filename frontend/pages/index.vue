<template>
  <div class="container">
    <header class="header">

      <div class="logo">
        <img src="~assets/public/img/logo-no-background.svg" alt="LOGO HERE" style="width: 25vw; height: auto;">
      </div>

      <div class="about-button">
        <button @click="to_aboutpage">О себе</button>
      </div>

      <div class="course-button">
        <button @click="to_coursepage">Курс</button>
      </div>

      <div class="auth-buttons">
        <button @click="login">Войти</button>
        <button @click="register">Зарегистрироваться</button>
      </div>

    </header>
  </div>
</template>

<script>
import { useRouter } from 'vue-router';
import { defineComponent } from 'vue';

export default defineComponent({
  setup() {
    const router = useRouter();

    const login = () => {
      router.push('/login');
    };

    return {
      login
    };
  },
});
</script>

<style scoped>
.container {
  font-family: Arial, sans-serif;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background: linear-gradient(to right, rgb(231, 166, 14), rgb(76, 76, 82));
}

.auth-buttons button {
  margin-left: 10px;
  background: transparent;
  border: none;
  color: white;
  cursor: pointer;
  transition: transform 0.2s;
}

.auth-buttons button:hover {
  transform: scale(1.1);
}
</style>