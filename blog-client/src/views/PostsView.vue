<script setup>
import { ref, onMounted } from 'vue'
import config from '../config'
import PostList from '../components/PostList.vue'

const posts = ref([])

onMounted(() => {
  fetch(`${config.apiBaseUrl}/posts`)
    .then(data => data.json())
    .then(json => posts.value = json.posts)
})
</script>
    
<template>
  <main>
    <hr />
    <h1>Posts</h1>
    <hr />
    <PostList :posts="posts" />
  </main>
</template>
    