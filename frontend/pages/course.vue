<template>
    <div class="course-container">
      <!-- Блок содержания слева -->
      <div class="contents">
        <h2>Chapters</h2>
        <ul>
          <li><strong>Lesson</strong></li>
        </ul>
      </div>
  
      <!-- Блок основного контента справа -->
      <div class="main-content">
        <h1>Course: Mastering Nuxt</h1>
        <div class="lesson">
          <h3><strong>Lesson</strong></h3>
          <p>This is a lesson:</p>

          <NuxtPage />

        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'CoursePage'
  }
  </script>
  
  <style scoped>
  .course-container {
    display: flex;
    min-height: 100vh;
  }
  
  .contents {
    width: 250px;
    padding: 2rem;
    background-color: #f8f8f8;
    border-right: 1px solid #e0e0e0;
  }
  
  .main-content {
    flex: 1;
    padding: 2rem;
    max-width: 800px;
    margin: 0 auto;
  }
  
  h1 {
    color: #2c3e50;
    margin-bottom: 1.5rem;
  }
  
  h2 {
    color: #34495e;
    margin-bottom: 1rem;
  }
  
  h3 {
    color: #2c3e50;
    margin-bottom: 0.5rem;
  }
  
  ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  li {
    padding: 0.5rem 0;
  }
  
  .lesson {
    background-color: #f5f5f5;
    padding: 1.5rem;
    border-radius: 4px;
    margin-top: 1rem;
  }
  </style>