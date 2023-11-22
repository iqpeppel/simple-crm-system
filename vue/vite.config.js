import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': '/src'
    }
  },
  server: {
    port : 8001,
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000/', // 修改为正确的目标域名
        changeOrigin: true,
        //rewrite: (path) => path.replace(/^\/api/, ''),
      },
    },
  },
   base: "./"
});

