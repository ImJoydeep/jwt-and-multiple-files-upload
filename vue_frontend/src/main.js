import './assets/main.css'
import axios from 'axios'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/index.js'

axios.defaults.baseURL= 'http://127.0.0.1:8000'
const app = createApp(App)
app.use(store)
app.use(router)

app.mount('#app')
