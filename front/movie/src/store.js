import Vue from 'vue'
import Vuex from 'vuex'
import testModule from './store/modules/testModule'
import testSubModule from './store/modules/testSubModule'
import indexModule from './store/modules/indexModule'

Vue.use(Vuex)

const store = new Vuex.Store({
    strict: process.env.NODE_ENV !== 'production',
    modules: {
      subModule1: testSubModule,
      subModule2: testSubModule,
      index: indexModule,
      testModule
    },
    state: {

    },
    mutations: {

    },
    actions: {

    }
})
/* eslint-disable no-console */
store.dispatch('testModule/testAction', ['subModule1', 'subModule2'])

export default store

