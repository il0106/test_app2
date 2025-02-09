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
  export default {
    
    methods: {
      login() {
        // Логика для кнопки "Войти"
      },
      register() {
        // Логика для кнопки "Войти"
      },
      scrollTo(section) {
        const element = document.getElementById(section);
        if (element) {
          element.scrollIntoView({ behavior: 'smooth' });
        }
      },
      nextImage() {
        this.currentIndex = (this.currentIndex + 1) % this.images.length;
      },
      prevImage() {
        this.currentIndex = (this.currentIndex - 1 + this.images.length) % this.images.length;
      },
    },
  }
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
  
  .auth-button button, .nav button {
    margin-left: 10px;
    background: transparent;
    border: none;
    color: white;
    cursor: pointer;
    transition: transform 0.2s;
  }
  
  .auth-button button:hover{
    transform: scale(1.1);
  }
 
  </style>