import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import TestPage from './components/Pages/TestPage.vue'
import MoviePage from './components/Pages/MoviePage.vue'
import DashBoardPage from './components/Pages/DashBoardPage.vue'
import LoginPage from './components/Pages/LoginPage.vue'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'home',
            component: HelloWorld
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
    ]
})

