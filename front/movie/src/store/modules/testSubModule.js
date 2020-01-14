const state = () => ({
    step: 1,
    count: 0,
    msg: "testSubModuleComponent"
})

const getters = {
    step: state => state.step,
    count: state => state.count,
    msg: state => state.msg
}

const actions = {
    testAction({ commit }) {
        commit('testMutation')
    }
}

const mutations = {
    testMutation(state) {
        state.count += state.step
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}
