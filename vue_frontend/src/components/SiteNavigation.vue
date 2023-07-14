<template>
  <header
    class="sticky top-0 bg-gradient-to-l from-teal-700 to-blue-700 shadow-lg"
  >
    <nav
      class="container flex flex-col sm:flex-row items-center gap-4 text-white py-6"
    >
      <RouterLink :to="{ name: 'home' }">
        <div class="flex items-center gap-3">
          <font-awesome-icon :icon="['fas', 'globe']" size="2xl" />
          <p class="text-2xl text-blue-100">Website</p>
        </div>
      </RouterLink>
      <div v-if="store.state.isAuthenticated" class="flex gap-3 flex-1 justify-end hover:cursor-pointer">
        <font-awesome-icon :icon="['fass', 'user']" size="2xl" @click="toggleModal"></font-awesome-icon>
        <BaseModal :modalActive="modalActive" @close-modal="toggleModal">
          <div class="grid text-black justify-items-center">
            <h3 class="text-xl text-blue-800">User Profile</h3>
            <i class="fa-solid fa-user text-4xl my-1"></i>
            <h2 class="text-xl my-1">Name: <strong>{{store.state.name}}</strong></h2>
            <h3 class="text-md my-1">Email: <strong>{{store.state.email}}</strong></h3>
          </div>
        </BaseModal>
      </div>
      <div v-else class="flex gap-3 flex-1 justify-end">Welcome, Guest</div>
    </nav>
  </header>
</template>

<script setup>
import { ref } from "vue";
import { RouterLink } from "vue-router";
import BaseModal from "./BaseModal.vue";
import { useStore } from "vuex";

const store = useStore()

const name = localStorage.getItem('name')
const email = localStorage.getItem('email')

const modalActive = ref(null);
const toggleModal = () => {
  modalActive.value = !modalActive.value;
};
</script>
