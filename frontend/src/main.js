import { createApp } from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';

import store from './store';
import router from './router';
import App from './App';

const app = createApp(App);
app.use(store);
app.use(router);
app.use(VueAxios, axios);

app.mount('#app');
