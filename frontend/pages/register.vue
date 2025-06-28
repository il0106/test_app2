<template>
    <div>
      <h1>Register</h1>
      <RegisterForm />
      <p>Already have an account? <nuxt-link to="/login">Login</nuxt-link></p>
    </div>
  </template>
  
  <script>
  import RegisterForm from '@/components/RegisterForm'
  
  export default {
    components: {
      RegisterForm,
    },
    middleware: 'guest', // Можно создать middleware для перенаправления аутентифицированных пользователей
  }
  </script>