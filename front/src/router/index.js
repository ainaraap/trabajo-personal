import { createRouter, createWebHistory } from 'vue-router'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/home/HomePage.vue'),
  },
  {
    path: '/dollsCatalog',
    name: 'Dolls',
    component: () => import('@/pages/dollsCatalog/DollsCatalogPage.vue'),
  },
  {
    path: '/dollDetail/:doll_id',
    name: 'Detail',
    component: () => import('@/pages/dollDetail/DollDetailPage.vue'),
  },
  {
    path: '/admin',
    name: 'Admin',
    component: () => import('@/pages/admin/AdminPage.vue'),
  },
  {
    path: '/form',
    name: 'Form',
    component: () => import('@/pages/form/FormMessagesPage.vue'),
  },
  {
    path: '/messagesList',
    name: 'MessagesList',
    component: () => import('@/pages/messages/ListMessagesPage.vue'),
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
