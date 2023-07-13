import { createStore } from "vuex";

export default createStore({
  state: {
    isAuthenticated: false,
    access: "",
    refresh: "",
  },
  getters: {},
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem("access")) {
        state.access = localStorage.getItem("access");
        state.isAuthenticated = true;
      } else {
        state.access = "";
        state.isAuthenticated = false;
      }
    },
    setAccess(state, access) {
      state.access = access;
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.access = "";
      state.isAuthenticated = false;
    },
  },
  actions: {},
  modules: {},
});
