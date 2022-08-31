<script setup>
    import { defineProps } from 'vue'
    import { RouterLink } from 'vue-router'

    const props = defineProps(['post'])
</script>

<template>
    <li>
        <RouterLink :to="`/post/${post.slug}`">{{ post.title }}</RouterLink>
    </li>
</template>
    