// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: false },
  ssr: true,

  devServer: {
    port: parseInt(process.env.FRONTEND_PORT || '3000'),
  },

  app: {
    head: {
      script: [
        {
          src: 'https://yastatic.net/s3/passport-sdk/autofill/v1/sdk-suggest-with-polyfills-latest.js',
          async: true,
          defer: true,
        },
      ],
    },
  },

  runtimeConfig: {
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE || process.env.BACKEND_API || 'http://localhost:8000'
    }
  },
  nitro: {
    envDir: '../',
    devProxy: {
      '/api': {
        target: process.env.BACKEND_API || 'http://localhost:8000',
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
      '/**': { cache: { swr: true, maxAge: 5 } } // Кэшировать все страницы на ... секунд
    }
  }
});