<template>
    <div class="container mx-auto">
  <div class="flex justify-center items-center py-10">
    <form
      @submit.prevent="loginUser"
      class="p-16 rounded shadow-lg bg-slate-50"
    >
      <div class="text-center font-bold text-2xl my-2">Login Form</div>
      <div class="mb-4">
        <label for="Email" class="block text-gray-700 text-sm font-bold mb-2"
          >Email:</label
        >
        <input
          type="email"
          placeholder="Email Address"
          id="Email"
          v-model="formData.email"
          required
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        />
      </div>

      <div class="mb-4">
        <label for="password" class="block text-gray-700 text-sm font-bold mb-2"
          >Password:</label
        >
        <input
          type="password"
          placeholder="Password"
          id="password"
          v-model="formData.password"
          required
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        />
      </div>
          <!-- Render the captcha form here -->
          <!-- <div v-html="captchaForm.captcha" class="mb-4"></div> -->

          <div class="mb-2 ">
          <label for="captcha" class="mt-2.5 text-gray-700 text-sm font-bold mb-2 w-1/2">Captcha:-</label>
          <p class="mt-2 mx-2 bg-amber-200 rounded line-through font-bold w-1/2">{{ captchaForm }}</p>
          <input type="text" v-model="formData.captcha" required id="captcha" placeholder="Enter The Numbers" class=" w-full shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
        </div>

      <div class="flex justify-center">
        <button
          type="submit"
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded"
        >
          Login
        </button>
      </div>
      <p class="text-green-600 text-md text-center" v-if="message">
        {{ message }}, redirecting...
      </p>
      <div>
      <p class="text-red-600 text-md text-center" v-if="errors">{{ errors }}
        ! Try Again
      </p>
    </div>
    <p class="my-2"><RouterLink to="/forgetpassword" class="text-blue-700">Forgotten password?</RouterLink></p>
    <p class="bg-green-500 hover:bg-green-700 text-white font-bold py-3 px-6 rounded"><RouterLink to="/register" class="text-white">Register Now</RouterLink></p>
    </form>
  </div>
</div>
</template>None

<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useStore } from 'vuex';
import { useRouter } from "vue-router";

const store = useStore()
const router = useRouter();
const message = ref("");
const err = ref(false);
const errors = ref('')
const captchaForm = ref('');



const formData = {
  email: "",
  password: "",
  captcha: "",
};

const loginUser = (e) => {
  axios.defaults.headers.common['Authorization'] = ''
  localStorage.removeItem('access')
  localStorage.removeItem('refresh')
  axios
    .post("/auth/login/", formData)
    .then((response) => {
      // Registration successful 
      errors.value = null
      err.value = false;
      // console.log(response.data.username)
      const access = response.data.token.access;
      store.commit('setAccess', access)
      axios.defaults.headers.common['Authorization'] = 'JWT ' + access
      localStorage.setItem('access', access);
      const refresh = response.data.token.refresh;
      message.value = response.data.msg;
      console.log(message); // Show success message to the user
      setTimeout(() => {
        router.push("/");
      }, 1000);
    })
    .catch((error) => {
      // Registration failed
      err.value = true;
      errors.value = error.response.data.errors.fields
      console.log(error.response.data.errors.fields)
      // Handle error and show appropriate feedback to the user
    });
};

const MAX_RELOAD_ATTEMPTS = 3;
let reloadAttempts = 0;

async function reloadPage() {
  try {
    const response = await axios.get("/auth/get_captcha/");
    captchaForm.value = response.data;
    console.log(response.data);
    if (captchaForm.value === '') {
      if (reloadAttempts < MAX_RELOAD_ATTEMPTS) {
        reloadAttempts++;
        reloadPage(); // Retry the reload
      } else {
        console.log('Maximum reload attempts reached. Unable to load captcha.');
      }
    }
  } catch (error) {
    console.error(error);
  }
}

onMounted(() => {
  reloadPage();
});


</script>