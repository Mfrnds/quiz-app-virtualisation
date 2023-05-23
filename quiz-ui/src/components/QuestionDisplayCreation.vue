<template>
  <form v-on:submit.prevent="submitForm" class="main-container pt-4">
    <div class="row">
      <h1 class="main-title">Création d'une nouvelle question</h1>
      <hr />
    </div>
    <div class="row my-2">
      <label for="questionPosition" class="mb-2">Position de la question</label>
      <div class="col-12">
        <input
          type="number"
          id="questionPosition"
          v-model="questionPosition"
          class="form form-control"
          placeholder="Position de la question"
          required="required"
        />
      </div>
    </div>
    <div class="row my-2">
      <label for="questionTitle" class="mb-2">Titre de la question</label>
      <div class="col-12">
        <input
          type="text"
          id="questionTitle"
          v-model="questionTitle"
          class="form form-control"
          placeholder="Titre de la question"
          required="required"
        />
      </div>
    </div>
    <div class="row my-2">
      <label for="questionImage" class="mb-2">Image illustrant la question</label>
      <div class="col-12">
        <center><img :src="questionImage" /></center>
        <input
          type="file"
          @change="handleImage"
          accept="image/*"
          class="form-control"
          id="questionImage"
          name="questionImage"
        />
      </div>
    </div>
    <div class="row my-2">
      <label for="questionText" class="mb-2">Intitulé de la question</label>
      <div class="col-12">
        <input
          type="text"
          id="questionText"
          v-model="questionText"
          class="form form-control"
          placeholder="Texte de la question"
          required="required"
        />
      </div>
    </div>
    <div class="row my-2">
      <label class="mb-2">Réponses proposées</label>
    </div>
    <div class="row justify-content-center" v-for="i in 4" v-bind:key="i">
      <div class="row mb-3">
        <div class="col-auto">
          <input
            type="radio"
            v-model="isCorrect"
            :value="i"
            required="required"
            :checked="i == 1 ? true : false"
          />
        </div>
        <div class="col-lg">
          <input
            type="text"
            class="form-control w-100"
            v-model="answers[i]"
            :placeholder="'Intitulé de la réponse n°' + i + ''"
            required="required"
          />
        </div>
      </div>
    </div>
    <div class="row justify-content-end my-2">
      <div class="col-4 text-end me-2">
        <button class="btn btn-primary main-btn me-3" id="saveQuestion">Sauvegarder</button>
        <router-link to="/admin" class="btn btn-primary main-btn">Annuler</router-link>
      </div>
    </div>
  </form>
</template>

<script>
import QuizApiService from '../services/QuizApiService'
import Swal from 'sweetalert2'

export default {
  name: 'QuestionDisplayCreation',
  data() {
    return {
      questionTitle: '',
      questionText: '',
      questionPosition: '',
      questionImage: '',
      isCorrect: 0,
      answers: []
    }
  },
  methods: {
    handleImage(e) {
      const selectedImage = e.target.files[0]
      this.createBase64Image(selectedImage)
    },
    createBase64Image(image) {
      const reader = new FileReader()
      reader.onload = (e) => {
        this.questionImage = 'data:image/png;base64,' + btoa(e.target.result)
      }
      reader.readAsBinaryString(image)
    },
    async submitForm() {
      let formatedAnswers = []
      let index = 1

      this.answers.forEach((element) => {
        formatedAnswers.push({
          text: element,
          isCorrect: index == this.isCorrect ? 1 : 0
        })
        index++
      })

      let postResponse = await QuizApiService.postNewQuestion(
        this.questionTitle,
        this.questionImage,
        this.questionText,
        this.questionPosition,
        formatedAnswers
      )

      if (postResponse.status === 200) {
        Swal.fire('Ajouté !', '', 'success').then((result) => {
          if (result.isConfirmed) {
            window.location = '/admin'
          }
        })
      } else if (postResponse.status === 401) {
        Swal.fire('Oops !', 'Votre connexion a expiré, veuillez-vous reconnecter', 'error').then(
          (result) => {
            if (result.isConfirmed) {
              this.$router.push('/login')
            }
          }
        )
      }
    }
  }
}
</script>
