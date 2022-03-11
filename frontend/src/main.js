import { createApp } from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';

import '../scss/custom.scss';
import 'bootstrap';

import store from './store';
import router from './router';
import App from './App';
import setupInterceptors from './common/interceptors';

setupInterceptors();

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

const app = createApp(App);
app.use(store);
app.use(router);
app.use(VueAxios, axios);

app.mount('#app');
