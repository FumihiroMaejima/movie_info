import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld.vue'
import TestPage from '@/components/pages/TestPage.vue'
import MoviePage from '@/components/pages/MoviePage.vue'
import DashBoardPage from '@/components/pages/DashBoardPage.vue'
import About from '@/components/pages/About.vue'
import LoginPage from '@/components/pages/LoginPage.vue'
import IndexPage from '@/components/pages/IndexPage.vue'
import NotFoundPage from '@/components/pages/NotFoundPage.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: IndexPage
    },
    {
      path: '/test',
      name: 'test',
      component: TestPage
    },
    {
      path: '/movie',
      name: 'movie',
      component: MoviePage
    },
    {
      path: '/login',
      name: 'login',
      component: LoginPage
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashBoardPage
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '*',
      name: 'notFound',
      component: NotFoundPage
    },
  ]
})

