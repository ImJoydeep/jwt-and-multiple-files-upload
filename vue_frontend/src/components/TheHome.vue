<template>
  <div class="container mx-auto">
    <h1 class="text-2xl text-gray-800 font-bold text-center my-6">
      Welcome, User
    </h1>
    <div class="flex flex-col items-center">
      <label
        class="relative cursor-pointer bg-cyan-400 rounded-md py-2 px-4 text-white"
      >
        <span class="absolute inset-0 opacity-0 cursor-pointer">
          <input
            type="file"
            ref="file"
            class="w-full h-full absolute inset-0 opacity-0 cursor-pointer"
            @change="selectFile"
            multiple
          />
        </span>
        <span class="file-label">Choose a file</span>
      </label>
    </div>
    <div class="flex justify-center my-4">
      <button
        type="submit"
        v-if="documents.length"
        @click="upload"
        class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
      >
        Upload
      </button>
    </div>
    <ul v-if="documents.length" class="mt-6 flex flex-wrap gap-4">
      <li
        class="text-ellipsis overflow-hidden w-1/1 md:w-1/4 lg:w-1/4 xl:w-1/4"
        v-for="document in documents"
        :key="document.name"
      >
        <img
          v-if="document.imageURL"
          :src="document.imageURL"
          alt="Selected Image"
          height="240"
          width="240"
          class="mt-2"
          />
          {{ document.name }} -
          <span class="font-semibold" :class="getStatusClass(document.status)"
          >{{ document.status }}.</span
          >
          <progress
          class="flex progress text-green-400 items-center my-2 rounded-xl"
          :value="document.progress"
          max="100"
          >
        </progress>
        {{ document.progress }}%
      </li>
    </ul>
  </div>
</template>
<script setup>
import { onMounted, ref } from "vue";
import axios from "axios";


const documents = ref([]);
const progress = ref(0);
const message = ref("");
const selectFile = (event) => {
  Array.from(event.target.files).forEach((file) => {
    const imageURL = URL.createObjectURL(file);
    documents.value.push({
      name: file.name,
      status: "is ready to upload",
      progress: 0,
      imageURL: imageURL,
    });
  });
};

const upload = async () => {
  for (const document of documents.value) {
    if (document.status === "is ready to upload") {
      document.status = "is uploading";

      const file = document.name;
      const formData = new FormData();
      formData.append("document", file);

      const config = {
        headers: {
          "Content-Type": "multipart/form-data",
          "X-CSRFToken": "{{ csrf_token }}",
        },
        onUploadProgress: (progressEvent) => {
          document.progress = Math.round(
            (progressEvent.loaded * 100) / progressEvent.total
          );
        },
      };

      try {
        await axios.post("auth/upload/", formData, config);
        document.status = "is uploaded";

        console.log(document.status);
      } catch (error) {
        document.status = "failed";
      }
    }
  }
  console.log(documents);
};

const getStatusClass = (status) => {
  if (status === "is ready to upload") {
    return "status-blue";
  } else if (status === "is uploaded") {
    return "status-green";
  } else if (status === "failed") {
    return "status-red";
  }
  return "";
};


</script>

<style>
.status-blue {
  color: rgb(237, 213, 0);
}

.status-green {
  color: rgb(3, 237, 3);
}
.status-red {
  color: rgb(194, 13, 13);
}
</style>
