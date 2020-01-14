const state = () => ({ modules: [] })

const getters = {
    count(state, getters, rootState) {
        //return rootState.counter.count + rootState.doubleCounter.count
        let sum = 0
        /* eslint-disable no-console */
        state.modules.forEach((elem) => {
            sum += rootState[elem].count
        })
        return sum
    }
}

const actions = {
    testAction({ commit }, val) {
        commit('setModules', val)
    }
}

const mutations = {
    setModules(state, val) {
        state.modules = val
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}
