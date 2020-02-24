/* eslint-disable no-undef */
import { shallowMount, createLocalVue } from '@vue/test-utils'
import Vuetify from 'vuetify'
import CardMovieSearch from '@/components/molecules/CardMovieSearch.vue'

const localVue = createLocalVue()
localVue.use(Vuetify)

const wrapper = shallowMount(CardMovieSearch, {
  localVue
})

describe('CardMovieSearch test', () => {
  it('checkDisabledData param null', () => {
    expect(wrapper.vm.checkDisabledData(null)).toBeTruthy()
  })
  it('checkDisabledData param not null', () => {
    expect(wrapper.vm.checkDisabledData(1)).toBeFalsy()
  })
})
