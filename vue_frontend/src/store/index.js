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
      // Local storage should only be used to store non-sensitive data like users' preferences such as themes, languages, etc.
      // You can use API calls to retrieve other important information and then set to state 
      if (localStorage.getItem("access")) {
        state.access = localStorage.getItem("access");
        state.name = localStorage.getItem("name");
        state.email = localStorage.getItem("email");
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
