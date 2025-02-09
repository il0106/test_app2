<template>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

onMounted(() => {
  // Проверяем наличие токена или необходимой информации после редиректа
  const hash = window.location.hash;
  const token = new URLSearchParams(hash.substring(1)).get('access_token');

  if (token) {
    localStorage.setItem('yid_token', token);
    window.close();
  } else {
    console.log('Ошибка авторизации');
  }
});
</script>
    