import { createRouter, createWebHistory } from 'vue-router';

import Home from '../views/Home';
import Contact from '../views/Contact';
import Listings from '../views/Listings';
import Login from '../views/Login';
import Account from '../views/Account';
import PasswordResetConfirm from '../views/PasswordResetConfirm';

const routes = [
  { path: "/", component: Home },
  { path: "/contact", component: Contact },
  { path: "/listings", component: Listings },
  { path: "/login", component: Login },
  {
    path: "/account", component: Account, children: [
      { path: "/password-reset/confirm/:userId/:token", component: PasswordResetConfirm },
    ]
  },
  { path: '/:pathMatch(.*)*', redirect: "/" },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;