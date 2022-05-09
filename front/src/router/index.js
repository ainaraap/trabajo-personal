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
    path: '/dollDetail',
    name: 'Detail',
    component: () => import('@/pages/dollDetail/DetailPage.vue'),
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
