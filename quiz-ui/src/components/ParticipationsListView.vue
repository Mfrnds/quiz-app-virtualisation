<template>
  <div class="row justify-content-end align-items-center mb-2">
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
              <th scope="col">Nom utitilisateur</th>
              <th scope="col">Score</th>
              <th scope="col">Date de participation</th>
            </tr>
          </thead>
          <tbody>
            <div class="row text-center" v-if="participations.length === 0">
              <span class="text-center">Aucune participations</span>
            </div>
            <tr v-else v-for="participation in participations" v-bind:key="participation.id">
              <th>{{ participation.playerName }}</th>
              <td>{{ participation.score }}</td>
              <td>{{ participation.date }}</td>
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
  name: 'ParticipationsListView',
  data() {
    return {
      participations: []
    }
  },
  async created() {
    let participationsData = await QuizApiService.getQuizInfo()
    this.participations = participationsData.data.scores
  },
  methods: {
    handleDeleteAll() {
      Swal.fire({
        title: 'Voulez-vous supprimer toutes les participations ?',
        showDenyButton: true,
        confirmButtonText: 'Oui',
        denyButtonText: 'Non'
      }).then((result) => {
        if (result.isConfirmed) {
          QuizApiService.deleteParticipations().then((result) => {
            if (result.status === 204) {
              Swal.fire('Participations supprimées !', '', 'success').then(() => {
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
