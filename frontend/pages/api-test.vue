<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-bold mb-4">API Test Page</h1>
    
    <!-- User Registration -->
    <div class="mb-8 p-4 border rounded">
      <h2 class="text-xl font-semibold mb-2">User Registration</h2>
      <form @submit.prevent="registerUser" class="space-y-2">
        <input v-model="registerForm.email" type="email" placeholder="Email" class="border p-2 w-full" />
        <input v-model="registerForm.password" type="password" placeholder="Password" class="border p-2 w-full" />
        <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded">Register</button>
      </form>
      <div v-if="registerForm.email || registerForm.password" class="mt-2 p-2 bg-gray-50">
        <h3 class="font-medium mb-1">Sent Data:</h3>
        <pre>{{ JSON.stringify(registerForm, null, 2) }}</pre>
      </div>
      <div v-if="registerResponse" class="mt-2 p-2 bg-gray-100">
        <h3 class="font-medium mb-1">Response:</h3>
        <pre>{{ registerResponse }}</pre>
      </div>
    </div>

    <!-- User Login -->
    <div class="mb-8 p-4 border rounded">
      <h2 class="text-xl font-semibold mb-2">User Login</h2>
      <form @submit.prevent="loginUser" class="space-y-2">
        <input v-model="loginForm.username" type="email" placeholder="Email" class="border p-2 w-full" />
        <input v-model="loginForm.password" type="password" placeholder="Password" class="border p-2 w-full" />
        <button type="submit" class="bg-green-500 text-white px-4 py-2 rounded">Login</button>
      </form>
      <div v-if="loginForm.username || loginForm.password" class="mt-2 p-2 bg-gray-50">
        <h3 class="font-medium mb-1">Sent Data:</h3>
        <pre>{{ JSON.stringify(loginForm, null, 2) }}</pre>
      </div>
      <div v-if="loginResponse" class="mt-2 p-2 bg-gray-100">
        <h3 class="font-medium mb-1">Response:</h3>
        <pre>{{ loginResponse }}</pre>
      </div>
    </div>

    <!-- Protected Route Test -->
    <div class="mb-8 p-4 border rounded">
      <h2 class="text-xl font-semibold mb-2">Protected Route Test</h2>
      <button @click="testProtectedRoute" class="bg-purple-500 text-white px-4 py-2 rounded">Test Protected Route</button>
      <div v-if="protectedResponse" class="mt-2 p-2 bg-gray-100">
        <h3 class="font-medium mb-1">Response:</h3>
        <pre>{{ protectedResponse }}</pre>
      </div>
    </div>
  </div>
</template>

<script setup>
const config = useRuntimeConfig()
const apiBase = config.public.apiBase

const registerForm = ref({
  email: '',
  password: ''
})

const loginForm = ref({
  username: '',
  password: ''
})

const registerResponse = ref(null)
const loginResponse = ref(null)
const protectedResponse = ref(null)

const registerUser = async () => {
  try {
    const response = await fetch(`${apiBase}/auth/register`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(registerForm.value)
    })
    registerResponse.value = await response.json()
  } catch (error) {
    registerResponse.value = { error: error.message }
  }
}

const loginUser = async () => {
  try {
    const response = await fetch(`${apiBase}/auth/jwt/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: new URLSearchParams(loginForm.value)
    })
    loginResponse.value = await response.json()
    if (loginResponse.value.access_token) {
      localStorage.setItem('token', loginResponse.value.access_token)
    }
  } catch (error) {
    loginResponse.value = { error: error.message }
  }
}

const testProtectedRoute = async () => {
  try {
    const token = localStorage.getItem('token')
    if (!token) {
      protectedResponse.value = { error: 'No token found. Please login first.' }
      return
    }

    const response = await fetch(`${apiBase}/users/me`, {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })
    protectedResponse.value = await response.json()
  } catch (error) {
    protectedResponse.value = { error: error.message }
  }
}
</script> 