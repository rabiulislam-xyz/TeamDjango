import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    carouselPhotos : [],
    messages: [
      {id:1, sender: 'rabiul islam', recever: 'mahdi khan', content: 'my message my message', timestamp: new Date()},
      {id:2, sender: 'kabir khan', recever: 'mahdi khan', content: 'sdfsadfessage my message', timestamp: new Date()},
      {id:3, sender: 'kurrumala', recever: 'mahdi khan', content: 'essdfdfage my message', timestamp: new Date()},
      {id:4, sender: 'nannu mia', recever: 'mahdi khan', content: 'y message my message', timestamp: new Date()}
    ],
    groupMessages: [],
    subscribedGroups: [],
    allMembers: [], 
    user: null,
    token: '',
    loading: false,
    error: null
  },
  mutations: {
    setUser (state, payload) {
      state.user = payload
    },
    setToken (state, payload) {
      state.token = payload
    },
    setAllMembers (state, payload) {
      state.allMembers = payload
    },
    setGroupMessages (state, payload) {
      state.groupMessages = payload
    },
    setSubscribedGroups (state, payload) {
      state.subscribedGroups = payload
    },
    setLoading (state, payload) {
      state.loading = payload
    },
    setError (state, payload) {
      state.error = payload
    },
    clearError (state) {
      state.error = null
    }
  },
  actions: {
    setAllMembers ({commit}, members) {
      commit('setAllMembers', members)
    },
    setGroupMessages ({commit}, groupMessages) {
      commit('setGroupMessages', groupMessages)
    },
    setSubscribedGroups ({commit}, groups) {
      commit('setSubscribedGroups', groups)
    },
    login ({commit}, user) {
      commit('setUser', user)
    },
    setToken ({commit}, token) {
      commit('setToken', token)
    },
    logout ({commit}) {
      commit('setUser', null)
    },
    clearError ({commit}) {
      commit('clearError')
    }
  },
  getters: {
    user (state) {
      return state.user
    },
    token (state) {
      return state.token
    },
    allMembers (state) {
      return state.allMembers
    },
    groupMessages (state) {
      return state.groupMessages
    },
    messages (state) {
      return state.messages
    },
    subscribedGroups (state) {
      return state.subscribedGroups
    },
    loading (state) {
      return state.loading
    },
    error (state) {
      return state.error
    }
  }
})