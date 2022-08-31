<script setup>
    import { ref, onMounted } from 'vue'
    import config from '../config'
    import PostListItem from './PostListItem.vue'
    
    const posts = ref([])

    onMounted(() => {
        fetch(`${config.apiBaseUrl}/posts`)
            .then(data => data.json())
            .then(json => posts.value = json.posts)
    })
</script>

<template>
    <ul>
        <PostListItem v-for="post in posts" :key="post.slug" :post="post" />
    </ul>
</template>
    