import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import QuestionManager from '../views/QuestionManager.vue'
import EndQuizPage from '../views/EndQuizPage.vue'
import QuestionCreationPage from '../views/QuestionCreationPage.vue'
import QuestionViewPage from '../views/QuestionViewPage.vue'
import LoginPage from '../views/LoginPage.vue'
import QuestionListPage from '../views/QuestionListPage.vue'
import AdminService from '../services/AdminService'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/start-new-quiz-page',
      name: 'StartNewQuiz',
      component: NewQuizPage
    },
    {
      path: '/questions',
      name: 'QuestionPage',
      component: QuestionManager
    },
    {
      path: '/end-quiz',
      name: 'EndQuizPage',
      component: EndQuizPage
    },
    {
      path: '/admin/create-question',
      name: 'QuestionCreationPage',
      component: QuestionCreationPage,
      meta: { requiresAuth: true }
    },
    {
      path: '/admin/view-question/:id',
      name: 'QuestionViewPage',
      component: QuestionViewPage,
      props: { mode: 'view' },
      meta: { requiresAuth: true }
    },
    {
      path: '/admin/edit-question/:id',
      name: 'QuestionEditPage',
      component: QuestionViewPage,
      props: { mode: 'edit' },
      meta: { requiresAuth: true }
    },
    {
      path: '/admin/view-questions',
      name: 'QuestionListPage',
      component: QuestionListPage,
      meta: { requiresAuth: true }
    },
    {
      path: '/login',
      name: 'LoginPage',
      component: LoginPage
    }
  ]
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = AdminService.getToken() !== (undefined || null)
  if (to.matched.some((record) => record.meta.requiresAuth) && !isAuthenticated) {
    next('/login')
  } else {
    next()
  }
})

export default router
