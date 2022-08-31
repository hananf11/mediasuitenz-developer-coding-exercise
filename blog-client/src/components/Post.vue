<script setup>
const props = defineProps(['post'])
</script>

<template>
  <header>
    <hr>
    <h1>{{ post.title }}</h1>
    <hr>
  </header>
  <div v-html="post.html"></div>
  <footer>
    <hr>
    <p>Author: {{ post.author }}</p>
  </footer>
</template>
    