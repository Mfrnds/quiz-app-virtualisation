<template>
  <div class="container admin-container">
    <div
      class="row"
      style="
        padding-right: calc(var(--bs-gutter-x) * 0.5);
        padding-left: calc(var(--bs-gutter-x) * 0.5);
      "
    >
      <ul class="nav nav-underline">
        <li class="nav-item">
          <h4
            :class="'nav-link main-title ' + questionsActive"
            aria-current="page"
            @click="handleChangeTab('questions')"
          >
            Questions
          </h4>
        </li>
        <li class="nav-item">
          <h4
            :class="'nav-link main-title ' + participationsActive"
            @click="handleChangeTab('participations')"
          >
            Participations
          </h4>
        </li>
      </ul>
    </div>
    <div v-if="questions" class=""><QuestionListView /></div>
    <div v-else class=""><ParticipationsListView /></div>
  </div>
</template>

<script>
import QuestionListView from '../components/QuestionListView.vue'
import ParticipationsListView from '../components/ParticipationsListView.vue'
export default {
  name: 'AdminHomePage',
  components: { QuestionListView, ParticipationsListView },
  data() {
    return {
      questions: true,
      questionsActive: 'active',
      participationsActive: ''
    }
  },
  created() {
    this.questions = true
    this.questionsActive = 'active'
  },
  methods: {
    handleChangeTab(mode) {
      this.questions = mode === 'questions'
      this.questionsActive = mode === 'questions' ? 'active' : ''
      this.participationsActive = mode === 'questions' ? '' : 'active'
    }
  }
}
</script>
