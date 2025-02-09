<template>
<div>
    <p>Обработка токена...</p>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

onMounted(() => {
  const hash = window.location.hash;
  const token = new URLSearchParams(hash.substring(1)).get('access_token');

  if (token) {
    console.log('Токен получен:', token);
    // Сохраните токен в хранилище (например, в Pinia или localStorage)
    localStorage.setItem('yandex_token', token);
    // Перенаправьте пользователя на главную страницу или другую страницу
    router.push('/');
  } else {
    console.error('Токен не найден');
    // Обработка ошибки
  }
});
</script>
    