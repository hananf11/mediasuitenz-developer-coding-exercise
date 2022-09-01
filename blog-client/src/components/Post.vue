<script setup>
const props = defineProps(['post'])
</script>

<template>
  <header>
    <hr>
    <h1>Post: {{ post.title }}</h1>
    <hr>
  </header>
  <div v-html="post.html"></div>
  <footer>
    <hr>
    <p>Author: {{ post.author }}</p>
    <p>Tags: {{ post.tags?.join(', ') }}</p>
    <hr>
  </footer>
</template>
    