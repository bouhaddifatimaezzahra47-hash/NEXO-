import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'
import signup from './templates/signup.vue'
import login from './templates/login.vue'
import addProducts from './templates/add_products.vue'

const routes = [
  { path: '/signup', name: 'signup', component: signup },
  { path: '/login', name: 'login', component: login },
  { path: '/add_products', name: 'addProducts', component: addProducts },
  { path: '/', redirect: '/signup' },
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})

const app = createApp(App)
app.use(router)
app.mount('#app')