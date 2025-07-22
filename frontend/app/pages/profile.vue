<template>
    <div>
      <h1>Profile</h1>
      <p>Welcome, {{ user?.email }}</p>
      <LogoutButton />
    </div>
  </template>
  
  <script setup>
  import { useAuth } from '~/composables/useAuth'
  
  const { user } = useAuth()
  
  definePageMeta({
    middleware: 'auth'
  })
  </script>