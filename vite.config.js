import { defineConfig } from "vite";
import { resolve } from "path";

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, "index.html"),
        folivio: resolve(__dirname, "folivio.html")
      }
    }
  },
  server: {
    host: true
  },
  preview: {
    host: true
  }
});
