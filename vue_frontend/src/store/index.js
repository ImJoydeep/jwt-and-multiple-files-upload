import { createStore } from "vuex";

export default createStore({
  state: {
    isAuthenticated: false,
    access: "",
    refresh: "",
    name: null,
    email: null,
  },
  getters: {},
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem("access")) {
        state.access = localStorage.getItem("access");
        state.isAuthenticated = true;
      } else {
        state.access = "";
        state.name = null;
        state.email = null;
        state.isAuthenticated = false;
      }
    },
    setAccess(state, access) {
      state.access = access;
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.access = "";
      state.name = null;
      state.email = null;
      state.isAuthenticated = false;
    },
  },
  actions: {},
  modules: {},
});
