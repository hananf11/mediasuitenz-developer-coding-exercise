<script setup>
  import { useRoute } from 'vue-router'
  import { computed, onMounted, ref } from 'vue'
  import config from '../config'
  import Post from '../components/Post.vue'

  const route = useRoute()
  const postSlug = computed(() => route.params.slug)
  const post = ref({})

  onMounted(
    () => fetch(`${config.apiBaseUrl}/posts/${postSlug.value}`)
      .then(data => data.json())
      .then(json => {
        document.title = json.title
        post.value = json
      })
  )
</script>
    
<template>
  <main>
    <Post :post="post" />
  </main>
</template>
    