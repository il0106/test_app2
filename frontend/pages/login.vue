<template>
  <div>
    <button @click="handleAuth">Войти через Яндекс</button>
    <div id="buttonContainerId"></div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();


// Функция для инициализации авторизации
const handleAuth = () => {
  window.YaAuthSuggest.init(
    {
      client_id: "0c1ee06a816c4ed7b3a5ef93f8422190",
      response_type: "token",
       redirect_uri: "https://ilyastarkov.ru/callback"
    },
    "http://109.196.102.43",
    {
      view: "button",
      parentId: "buttonContainerId",
      buttonSize: 'xxl',
      buttonView: 'main',
      buttonTheme: 'light',
      buttonBorderRadius: "16",
      buttonIcon: 'ya',
    }
  )
  .then(({handler}) => handler());
};

let intervalId;

const checkForToken = () => {
  const token = localStorage.getItem('yid_token');
  if (token) {
    router.push('/workspace');
  }
};

onMounted(() => {
  checkForToken(); // Проверяем сразу при монтировании

  intervalId = setInterval(checkForToken, 1000); // Проверяем каждую секунду
});

onUnmounted(() => {
  clearInterval(intervalId); // Очищаем интервал при размонтировании
});
</script>