<template>
  <Teleport to="body">
    <Transition name="modal-outer">
      <div
        v-show="modalActive"
        class="absolute w-full bg-black bg-opacity-30 h-screen top-0 left-0 flex justify-center px-8"
      >
        <Transition name="modal-inner">
          <div
            v-if="modalActive"
            class="p-4 bg-blue-100 self-start mt-32 max-w-screen-md"
          >
            <slot />

            <button
              class="text-white mt-8 transition ease-in-out delay-150 hover:-translate-y-1 hover:scale-105 hover:bg-secondary duration-300 bg-gradient-to-r from-primary via-secondary to-primary hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-teal-300 dark:focus:ring-teal-800 shadow-lg shadow-teal-500/50 dark:shadow-lg dark:shadow-teal-800/80 font-medium rounded-lg text-sm px-6 py-2.5 text-center mr-2 mb-2"
              @click="$emit('close-modal')"
            >
              Close
            </button>
            <button 
              @click="logOut"
              class="mt-4 ml-24 text-white bg-gradient-to-r from-red-500 via-red-500 to-red-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-red-300 shadow-lg shadow-red-500/50 dark:shadow-lg font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2 transition ease-in-out delay-150 hover:-translate-y-1 hover:scale-105 hover:bg-weather-secondary duration-300"
            >
              Logout
            </button>
          </div>
        </Transition>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup>
import axios from "axios";
import router from "../router";


const emit = defineEmits(["close-modal"]);

defineProps({
  modalActive: {
    type: Boolean,
    default: false,
  },
});

const logOut = () => {
  if (localStorage.getItem("access")) {
    axios.defaults.headers.common["Authorization"] = ""
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    router.push("/login");
  }
  emit("close-modal");
};
</script>

<style scoped>
.modal-outer-enter-active,
.modal-outer-leave-active {
  transition: opacity 0.3s cubic-bezier(0.52, 0.02, 0.19, 1.02);
}

.modal-outer-enter-from,
.modal-outer-leave-to {
  opacity: 0;
}

.modal-inner-enter-active {
  transition: all 0.3s cubic-bezier(0.52, 0.02, 0.19, 1.02) 0.15s;
}

.modal-inner-leave-active {
  transition: all 0.2s cubic-bezier(0.52, 0.02, 0.19, 1.02);
}

.modal-inner-enter-from {
  opacity: 0;
  transform: scale(0.4);
}

.modal-inner-leave-to {
  transform: scale(0.4);
}
</style>
