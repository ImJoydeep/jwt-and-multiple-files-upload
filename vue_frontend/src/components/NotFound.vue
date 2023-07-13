<template>

    <div class="flex flex-col items-center justify-center mt-8">
      <img src="../assets/404.png" alt="Page Not Found" class="rounded-full border-transparent shadow-lg mb-8 animate-bounce">
      <h1 class="text-4xl text-amber-300 font-bold mb-4">Oops!</h1>
      <p class="text-lg mb-8 text-amber-200">The page you're looking for doesn't exist.</p>
      <router-link class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600" to="/">Go back to the home page </router-link>
    </div>
  </template>
  
  <script>
  </script>
  
  <style>
  @keyframes bounce {
    0%, 20%, 50%, 80%, 100% {
      transform: translateY(0);
    }
    40% {
      transform: translateY(-20px);
    }
    60% {
      transform: translateY(-10px);
    }
  }
  
  .animate-bounce {
    animation: bounce 2.5s ease-in-out infinite;
  }
  </style>
  