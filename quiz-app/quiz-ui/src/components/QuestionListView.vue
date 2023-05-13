<template>
  <div class="row justify-content-end align-items-center mb-2">
    <router-link to="/admin/create-question" class="badge col-6 second-badge me-3"
      ><i class="bi bi-plus"></i>Ajouter</router-link
    >
    <span class="badge col-6 second-badge me-3" @click="handleDeleteAll"
      ><i class="bi bi-x"></i>Tout supprimer</span
    >
  </div>
  <div class="card" style="height: 76vh">
    <div class="card-body" style="overflow: auto">
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
            <div class="row text-center" v-if="questions.length === 0">
              <span class="text-center">Aucune questions</span>
            </div>
            <tr v-else v-for="question in questions" v-bind:key="question.id">
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
</template>

<script>
import QuizApiService from '../services/QuizApiService'
import Swal from 'sweetalert2'

export default {
  name: 'QuestionListView',
  data() {
    return {
      questions: []
    }
  },
  async created() {
    let questionsData = await QuizApiService.getAllQuestions()
    console.log(questionsData)
    this.questions = questionsData.data
  },
  methods: {
    handleDeleteAll() {
      Swal.fire({
        title: 'Voulez-vous supprimer toutes les questions ?',
        showDenyButton: true,
        confirmButtonText: 'Oui',
        denyButtonText: 'Non'
      }).then((result) => {
        if (result.isConfirmed) {
          QuizApiService.deleteQuestions().then((result) => {
            if (result.status === 204) {
              Swal.fire('Questions supprimées !', '', 'success').then(() => {
                window.location = '/admin'
              })
            } else if (result.status === 401) {
              Swal.fire(
                'Oops !',
                'Votre connexion a expiré, veuillez-vous reconnecter',
                'error'
              ).then((result) => {
                if (result.isConfirmed) {
                  this.$router.push('/login')
                }
              })
            }
          })
        }
      })
    }
  }
}
</script>
