import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import QuestionManager from '../views/QuestionManager.vue'
import EndQuizPage from '../views/EndQuizPage.vue'
import QuestionCreationPage from '../views/QuestionCreationPage.vue'
import QuestionViewPage from '../views/QuestionViewPage.vue'
import LoginPage from '../views/LoginPage.vue'

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
      component: QuestionCreationPage
    },
    {
      path: '/admin/view-question/:id',
      name: 'QuestionViewPage',
      component: QuestionViewPage
    },
    {
      path: '/login',
      name: 'LoginPage',
      component: LoginPage
    }
  ]
})

export default router
