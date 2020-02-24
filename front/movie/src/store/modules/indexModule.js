const state = () => ({
  titles: [],
  searchData: '',
  MoviesData: {}
})

const getters = {
  titles: state => state.titles,
  searchData: state => state.searchData,
  MoviesData: state => state.MoviesData
}

const actions = {
  getTitlesDataAction({ commit }, payload) {
    commit('setTitlesData', payload)
  },
  getSearchDataAction({ commit }, payload) {
    commit('setSearchData', payload)
  },
  getMoviesDataAction({ commit }, payload) {
    commit('setMoviesData', payload)
  }
}

const mutations = {
  setTitlesData(state, payload) {
    state.titles = payload
  },
  setSearchData(state, payload) {
    state.searchData = payload
  },
  setMoviesData(state, payload) {
    state.MoviesData = payload
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
