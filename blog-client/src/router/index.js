import { createRouter, createWebHistory } from 'vue-router'
import PostsView from '../views/PostsView.vue'
import PostView from '../views/PostView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'posts',
      component: PostsView,
      meta: {
        title: 'Posts'
      }
    },
    {
      path: '/post/:slug',
      name: 'Post',
      component: PostView,
      meta: {
        title: "Post"
      }
    }
  ]
})

router.beforeEach((to) => {
  document.title = to.meta.title
})

export default router
