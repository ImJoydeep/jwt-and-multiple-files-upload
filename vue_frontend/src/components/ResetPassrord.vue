<template>
  <div class="container mx-auto">
    <div class="flex justify-center items-center py-10">
      <form
        @submit.prevent="submitForm"
        class="p-16 rounded shadow-lg bg-slate-50"
      >
      <div class="text-center font-bold text-2xl mb-4">Reset Password</div>
      <div class="mb-4">
        <label for="password" class="block text-gray-700 text-sm font-bold mb-2"
          >New Password:</label
        >
        <input
          type="password"
          placeholder="New Password"
          id="password"
          v-model="formData.password"
          required
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        />
      </div>      <div class="mb-4">
        <label for="password" class="block text-gray-700 text-sm font-bold mb-2"
          >Confirm Password:</label
        >
        <input
          type="password"
          placeholder="Confirm Password"
          v-model="formData.password2"
          required
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        />
      </div>
      <div class="flex justify-center">
        <button
          type="submit"
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded"
        >
          Submit
        </button>
      </div>
      <div class="">
        <p class="text-green-600" v-if="message">
        {{ message }}
      </p>
      <p class="text-red-600 text-md text-center" v-if="err">{{ err }}
        ! Try Again
      </p>
    </div>
    </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';


const router = useRoute()
const route = useRouter()

const message = ref('')
const err = ref('')
const formData = {
  password: "",
  password2: "",
};

const submitForm = () => {
  const { uid, token } = router.params;
  message.value = ''
  err.value = ''
  axios
    .post(`auth/reset-password/${uid}/${token}/`, formData)
    .then((response) => {
      // Password Reset successful 
      console.log(response.data.msg)// Show success message to the user
      message.value = response.data.msg
      setTimeout(()=>{route.push("/login");},1500)
    })
    .catch((error) => {
      // Password Reset failed
      console.log(error.response.data.errors.non_field_errors)
      err.value = error.response.data.errors.non_field_errors
      // Handle error and show appropriate feedback to the user
    });
  };
  
</script>

<style></style>
