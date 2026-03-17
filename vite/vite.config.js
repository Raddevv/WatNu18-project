import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    host: true,
    proxy: {
      '/api': {
        // In docker-compose, Vite runs in its own container.
        // Proxy to the chatbot service via the compose network.
        target: 'http://chatbot:8000',
        changeOrigin: true
      }
    }
  }
})
