<template>
  <div class="container mx-auto">
  <div class="flex justify-center items-center py-10">
    
    <form @submit.prevent="registerUser" class="bg-white p-16 rounded shadow-md">
      <div class="text-center font-bold text-2xl mb-4">Registration Form</div>
      <div class="mb-4">
        <label for="Email" class="block text-gray-700 text-sm font-bold mb-2"
          >Email:</label
        >
        <input
          type="email"
          id="Email"
          placeholder="Email Address"
          v-model="formData.email"
          required
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        />
      </div>
      <div class="mb-4">
        <label for="name" class="block text-gray-700 text-sm font-bold mb-2"
          >Name:</label
        >
        <input
          type="text"
          placeholder="Full Name"
          id="name"
          v-model="formData.name"
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
      <div class="mb-4">
        <label
          for="password2"
          class="block text-gray-700 text-sm font-bold mb-2"
          >Confirm Password:</label
        >
        <input
          type="password"
          placeholder="Confirm Password"
          id="password2"
          v-model="formData.password2"
          required
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        />
      </div>

      <div class="flex justify-center">
        <button
          type="submit"
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Register
        </button>
      </div>
      <p class="text-green-600 text-md text-center" v-if="message">{{ message }}, redirecting</p>
      <p class="text-red-600 text-md text-center" v-if="err">Registration Failed! Try Again</p>
      <p>Already have account? <RouterLink to="/login" class="text-blue-700">Login</RouterLink></p>
    </form>
  </div>
</div>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const message = ref('');
const err = ref(false);

const formData = {
  email: "",
  name: "",
  password: "",
  password2: "",
  tc: true,
};

const registerUser = () => {
  axios
    .post("/auth/register/", formData)
    .then((response) => {
      // Registration successful
      err.value = false
      const token = response.data.token;
      message.value = response.data.msg;
      console.log(token); // Do something with the token
      console.log(message); // Show success message to the user
    //   router.push("/login");
    setTimeout(()=>{router.push("/login");},1500)
    })
    .catch((error) => {
      // Registration failed
      console.error(error.response.data);
      err.value = true
      // Handle error and show appropriate feedback to the user
    });
};
</script>
