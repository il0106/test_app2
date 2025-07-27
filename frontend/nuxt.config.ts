import { config as dotenvConfig } from 'dotenv' // это работает при разработке
import { resolve } from 'path'

// Явно указываем путь до нужного .env-файла
dotenvConfig({ path: resolve(__dirname, '../.env') })


// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: false },
  ssr: true,

  devServer: {
    port: parseInt(process.env.FRONTEND_PORT),
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
      apiBase: process.env.BACKEND_API
    }
  },
  // nitro: {
  //   envDir: './', // при разраюотке envDir: './',
  //   // devProxy: {
  //   //   '/api': {
  //   //     target: process.env.BACKEND_API,
  //   //     changeOrigin: true,
  //   //     secure: false,
  //   //   },
  //   // },
  //   // storage: {
  //   //   'cache': {
  //   //     driver: 'fs',
  //   //     base: './.cache'
  //   //   }
  //   // },
  //   // routeRules: {
  //   //   '/**': { cache: { swr: true, maxAge: 5 } } // Кэшировать все страницы на ... секунд
  //   // }
  // }
});