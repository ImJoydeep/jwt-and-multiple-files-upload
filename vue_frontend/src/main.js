import './assets/main.css';
import axios from 'axios';
import { createApp } from 'vue';
import App from './App.vue';
import router from './router/index.js';
import store from './store/index.js';

import { library } from '@fortawesome/fontawesome-svg-core';
import { fas, faUserSecret} from '@fortawesome/free-solid-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
library.add(fas, far, fab, faUserSecret)

const app = createApp(App).component("font-awesome-icon", FontAwesomeIcon);

axios.defaults.baseURL= 'http://127.0.0.1:8000';
// axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('access');

app.use(store);
app.use(router,axios);
app.config.errorHandler = (err, instance, info) => {
    // report error to tracking services
    console.log(err)
    console.log(instance)
    console.log(info)
  }

app.mount('#app');
