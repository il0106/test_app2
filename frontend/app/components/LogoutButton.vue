<template>
  <button @click="logout" class="logout-button">
    <svg class="logout-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path>
    </svg>
    Выйти
  </button>
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

<style scoped>
.logout-button {
  background: #ef4444;
  color: white;
  border: none;
  padding: 15px 30px;
  border-radius: 10px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  width: 100%;
}

.logout-button:hover {
  background: #dc2626;
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(239, 68, 68, 0.3);
}

.logout-icon {
  width: 20px;
  height: 20px;
}
</style>