<template>
  <div id="app">
    <h1>Сумма двух чисел</h1>
    <input v-model.number="a" placeholder="Первое число" type="number" />
    <input v-model.number="b" placeholder="Второе число" type="number" />
    <button @click="calculateSum">Посчитать сумму</button>
    <p v-if="sum !== null">Сумма: {{ sum }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      a: null,
      b: null,
      sum: null,
    };
  },
  methods: {
    async calculateSum() {
      if (this.a !== null && this.b !== null) {
        try {
          const response = await fetch(`/api/sum?a=${this.a}&b=${this.b}`);
          const data = await response.json();
          this.sum = data.sum;
        } catch (error) {
          console.error("Ошибка:", error);
        }
      } else {
        alert("Введите оба числа.");
      }
    },
  },
};
</script>

<style>
#app {
  text-align: center;
  margin-top: 50px;
}
input {
  margin: 5px;
}
</style>