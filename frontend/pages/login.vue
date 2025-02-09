<!-- <template>
  <div>
    <button @click="handleConnect">Авторизоваться с помощью Яндекс ID</button>
  </div>
</template>

<script setup>
function handleConnect() {
  const authUrl = "https://oauth.yandex.ru/authorize?response_type=code&client_id=0c1ee06a816c4ed7b3a5ef93f8422190";
  
  // Открываем новое окно для авторизации
  const newWindow = window.open(
    authUrl,
    'new_window',
    'left=200,width=200,menubar=no'
  );

  // Если нужно, можно добавить обработчик для закрытия окна или получения данных
  if (newWindow) {
    newWindow.focus();
  }
}
</script>

<style scoped>
/* Ваши стили здесь */
button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
}
</style> -->




<template>
  <div>
    <button @click="handleAuth">Войти через Яндекс</button>
    <div id="buttonContainerId"></div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';

// Функция для инициализации авторизации
const handleAuth = () => {
  window.YaAuthSuggest.init(
    {
      client_id: "0c1ee06a816c4ed7b3a5ef93f8422190",
      response_type: "token",
      redirect_uri: "http://localhost:3000/callback"
    },
    "http://localhost",
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
  .then(({handler}) => handler())
  .then(data => console.log('Сообщение с токеном', data))
  .catch(error => console.log('Обработка ошибки', error));
};

// Инициализация при монтировании компонента
onMounted(() => {
  // Здесь можно выполнить дополнительную инициализацию, если необходимо
});
</script>
