<template>
  <div class="container mx-auto">
    <div class="flex justify-center items-center py-10">
      <form
        @submit.prevent="submitForm"
        class="p-16 rounded shadow-lg bg-slate-50"
      >
        <div class="text-center font-bold text-2xl my-2">Reset Form</div>
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
import axios from 'axios';
import { ref } from "vue";

const message = ref('')
const err = ref('')

const formData = {
  email: "",
};

const submitForm = () => {
  message.value = ''
  err.value = ''
  axios
    .post("/auth/send-reset-password-email/", formData)
    .then((response) => {
      // Password Reset successful 
      console.log(response.data.msg)// Show success message to the user
      message.value = response.data.msg
      // setTimeout(() => {
      //   router.push("/");
      // }, 1000);
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
