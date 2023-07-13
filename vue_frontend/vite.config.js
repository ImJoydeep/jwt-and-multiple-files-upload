import { defineConfig } from "vite";
import { fileURLToPath, URL } from "node:url";
import vue from "@vitejs/plugin-vue";

// export default defineConfig({
//   plugins: [vue()],
//   // base: '/joydeep/fileupload/vuefrontend/',
//   build: {
//     minify: true,
//     outDir: 'joydeep/fileupload/vuefrontend/',
//     assetsDir: 'assets',
//     sourcemap: false,
//   },
//   resolve: {
//     alias: {
//       '@': fileURLToPath(new URL('./src', import.meta.url))
//     },
//   },
// });

export default defineConfig(({ command, mode, ssrBuild }) => {
  console.log(command, mode, ssrBuild);
  if (mode === "production") {
    return {
      base: "/joydeep/fileupload/vuefrontend",
      plugins: [vue()],
      build: {
        minify: true,
        outDir: "dist",
        assetsDir: "assets",
        sourcemap: false,
      },
      resolve: {
        alias: {
          "@": fileURLToPath(new URL("./src", import.meta.url)),
        },
      },
    };
  }
  return {
    plugins: [vue()],
    resolve: {
      alias: {
        "@": fileURLToPath(new URL("./src", import.meta.url)),
      },
    },
  };
});
