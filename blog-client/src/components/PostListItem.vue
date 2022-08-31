<script setup>
    import { defineProps } from 'vue'

    const props = defineProps(['post'])
</script>

<template>
    <li>
        <a :href="`/posts/${post.slug}`">{{ post.title }}</a>
    </li>
</template>
    