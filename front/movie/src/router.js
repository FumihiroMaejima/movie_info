import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld.vue'
// import LoginPage from '@/components/pages/LoginPage.vue'
// import TestPage from '@/components/pages/TestPage.vue'
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
    /*
    {
      path: '/login',
      name: 'login',
      component: LoginPage
    },
    {
      path: '/test',
      name: 'test',
      component: TestPage
    },
    */
    {
      path: '*',
      name: 'notFound',
      component: NotFoundPage
    },
  ]
})

