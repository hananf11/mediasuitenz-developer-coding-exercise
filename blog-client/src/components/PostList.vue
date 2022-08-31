<script setup>
    import PostListItem from './PostListItem.vue';
    const props = defineProps(['posts'])    
</script>

<template>
    <ul>
        <PostListItem v-for="post in posts" :key="post.slug" :post="post" />
    </ul>
</template>
    