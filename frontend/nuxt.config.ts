// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  ssr: true,
  runtimeConfig: {
    public: {
      apiBaseUrl: 'http://localhost:8000'
    }
  },
  nitro: {
    devProxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        secure: false,
      },
    },
    storage: {
      'cache': {
        driver: 'fs',
        base: './.cache'
      }
    },
    routeRules: {
      '/**': { cache: { swr: true, maxAge: 30 } } // Кэшировать все страницы на ... секунд
    }
  }
});