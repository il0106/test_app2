<template>
  <div>
    <h1>Login</h1>
    <LoginForm />
    <p>Don't have an account? <nuxt-link to="/register">Register</nuxt-link></p>
  </div>
</template>

<script>
import LoginForm from '@/components/LoginForm'

export default {
  components: {
    LoginForm,
  },
  middleware: 'guest',
}
</script>