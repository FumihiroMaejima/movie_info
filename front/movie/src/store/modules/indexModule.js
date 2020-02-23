const state = () => ({
  titles: [],
  searchData: ''
})

const getters = {
  titles: state => state.titles,
  searchData: state => state.searchData
}

const actions = {
  getTitlesDataAction({ commit }, payload) {
    commit('setTitlesData', payload)
  },
  getSearchDataAction({ commit }, payload) {
    commit('setSearchData', payload)
  }
}

const mutations = {
  setTitlesData(state, payload) {
    state.titles = payload
  },
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
