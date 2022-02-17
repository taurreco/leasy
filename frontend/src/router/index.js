import { createRouter, createWebHistory } from 'vue-router';

import Home from '../views/Home';
import Contact from '../views/Contact';
import Listings from '../views/Listings';
import Login from '../views/Login';

const routes = [
  { path: "/", component: Home },
  { path: "/contact", component: Contact },
  { path: "/listings", component: Listings },
  { path: "/login", component: Login }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;