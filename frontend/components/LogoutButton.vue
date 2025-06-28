<template>
    <button @click="logout">Logout</button>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router'
  import { useRuntimeConfig } from 'nuxt/app'
  import { useAuth } from '~/composables/useAuth'
  
  const router = useRouter()
  const config = useRuntimeConfig()
  const { clearUser } = useAuth()
  
  const logout = async () => {
    try {
      await $fetch('/auth/jwt/logout', {
        method: 'POST',
        baseURL: config.public.apiBase,
      })
      
      // Clear user data and token
      clearUser()
      
      router.push('/login')
    } catch (err) {
      console.error('Logout failed:', err)
    }
  }
  </script>