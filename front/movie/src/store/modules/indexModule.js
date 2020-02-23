const state = () => ({
  searchData: ''
})

const getters = {
  searchData: state => state.searchData,
}

const actions = {
  getSearchDataAction({ commit }, payload) {
    commit('setSearchData', payload)
  }
}

const mutations = {
  setSearchData(state, payload) {
    state.searchData = payload
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
