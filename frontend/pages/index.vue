<template>
  <div class="container">
    <header class="header">
      <div class="logo">
        <img src="~assets/public/img/logo-no-background.svg" alt="LOGO HERE" style="width: 25vw; height: auto;">
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

    const register = () => {
      // Логика для регистрации, например, перенаправление на страницу регистрации
      router.push('/sum');
    };

    return {
      login,
      register,
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