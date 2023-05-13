<template>
  <div class="container admin-container">
    <div class="card" style="height: 76vh">
      <div class="card-body" style="overflow: auto">
        <div class="row justify-content-between align-items-center">
          <h2 class="col-6 main-title">Questions</h2>
          <router-link to="/admin/create-question" class="badge col-6 second-badge me-3"
            ><i class="bi bi-plus"></i>Ajouter</router-link
          >
        </div>
        <div class="row">
          <table class="table table-striped">
            <thead>
              <tr>
                <th scope="col">Titre</th>
                <th scope="col">Intitulé</th>
                <th scope="col"></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="question in questions" v-bind:key="question.id">
                <th>{{ question.title }}</th>
                <td>{{ question.text }}</td>
                <td>
                  <router-link
                    :to="'/admin/view-question/' + question.id"
                    class="badge second-badge me-3"
                    ><i class="bi bi-info-circle"></i
                  ></router-link>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import quizApiService from '../services/QuizApiService'

export default {
  name: 'QuestionListPage',
  data() {
    return {
      questions: []
    }
  },
  async created() {
    let questionsData = await quizApiService.getAllQuestions()
    console.log(questionsData)
    this.questions = questionsData.data
  }
}
</script>
