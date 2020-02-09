/* eslint-disable no-undef */
import Vue from 'vue'
import Vuetify from 'vuetify'
import { shallowMount } from '@vue/test-utils'
import CardMovieSearch from '@/components/molecules/CardMovieSearch.vue'

Vue.use(Vuetify)
const wrapper = shallowMount(CardMovieSearch)

describe('CardMovieSearch test', () => {
  it('checkDisabledData param null', () => {
    expect(wrapper.vm.checkDisabledData(null)).toBeTruthy()
  })
  it('checkDisabledData param not null', () => {
    expect(wrapper.vm.checkDisabledData(1)).toBeFalsy()
  })
})
