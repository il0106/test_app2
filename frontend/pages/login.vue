<template>
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
</style>