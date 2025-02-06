<template>
    <div class="container">
      <header class="header">
        <div class="logo">Логотип</div>
        <div class="auth-button"><button @click="login">Войти</button></div>
        <nav class="nav">
          <button @click="scrollTo('about')">О нас</button>
          <button @click="scrollTo('pricing')">Тарифы</button>
          <button @click="scrollTo('contacts')">Контакты</button>
        </nav>
      </header>
  
      <section class="hero">
        ![](https://chat.aiacademy.me/api/chats/gigachat_image/images[currentIndex])
        </div>
        <div class="carousel-controls">
          <button @click="prevImage">«</button>
          <button @click="nextImage">»</button>
        </div>
      </section>
  
      <section class="text-block" id="about">
        <h2>Заголовок блока</h2>
        <p>Ваш текст здесь.</p>
      </section>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        images: [
          'image1.jpg',
          'image2.jpg',
          'image3.jpg',
        ],
        currentIndex: 0,
      };
    },
    methods: {
      login() {
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
    background: linear-gradient(to right, orange, blue);
  }
  
  .auth-button button, .nav button {
    margin-left: 10px;
    background: transparent;
    border: none;
    color: white;
    cursor: pointer;
    transition: transform 0.2s;
  }
  
  .auth-button button:hover, .nav button:hover {
    transform: scale(1.1);
  }
  
  .hero {
    position: relative;
  }
  
  .hero-image {
    width: 100%;
    height: 100vh;
    object-fit: cover;
  }
  
  .hero-text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
    font-size: 48px;
    text-align: center;
  }
  
  .carousel {
    padding: 20px;
    background-color: #f0f0f0;
    text-align: center;
  }
  
  .carousel-container {
    display: inline-block;
  }
  
  .carousel-image {
    width: 80%;
    height: auto;
  }
  
  .carousel-controls {
    margin-top: 10px;
  }
  
  .text-block {
    padding: 20px;
    background: linear-gradient(to bottom, orange, gray);
    color: black;
  }
  </style>