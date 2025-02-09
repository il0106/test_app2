// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  ssr: true,
  app: {
    head: {
      script: [
        {
          src: 'https://yastatic.net/s3/passport-sdk/autofill/v1/sdk-suggest-with-polyfills-latest.js',
          defer: true,
        },
      ],
    },
  },
  // auth: {
  //   isEnabled: true,
  //   disableServerSideAuth: false,
  //   originEnvKey: 'AUTH_ORIGIN',
  //   baseURL: 'http://localhost:3000/api/auth',
  //   sessionRefresh: {
  //     enablePeriodically: true,
  //     enableOnWindowFocus: true,
  //   },
  //   provider: {
  //     type: 'authjs',
  //     trustHost: false,
  //     defaultProvider: 'github',
  //     addDefaultCallbackUrl: true
  //   },
  // },
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