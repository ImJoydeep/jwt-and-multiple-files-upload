<script setup>
import { RouterLink, RouterView } from 'vue-router'
import SiteNavigation from "./components/SiteNavigation.vue";

import axios from 'axios';
import { useStore } from 'vuex';

const store = useStore()

const beforeCreate = () => {
  store.commit('initializeStore')
  const access = store.state.access

  if (access) {
    axios.defaults.headers.common['Authorization'] = "JWT " + access
  } else {
    axios.defaults.headers.common['Authorization'] = ''
  }
}
</script>

<template>
  <div class="flex flex-col min-h-screen font-Roboto bg-primary">
  <SiteNavigation />
  <RouterView />
  </div>
</template>

<style>


nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}



</style>
