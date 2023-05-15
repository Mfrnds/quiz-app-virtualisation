<template>
  <div class="main-container pt-4">
    <div class="row justify-content-between">
      <div class="col-6">
        <h2 v-if="isView" class="main-title">Visualisation d'une question</h2>
        <h2 v-else class="main-title">Edition d'une question</h2>
      </div>
      <div v-if="isView" class="col-3">
        <span class="badge col-6 second-badge me-3" @click="handleEditClick"
          ><i class="bi bi-pen"></i>Editer</span
        >
        <span class="badge col-6 second-badge me-3" @click="handleDeleteClick"
          ><i class="bi bi-trash"></i>Supprimer</span
        >
      </div>
    </div>
    <hr />
    <div class="row my-2">
      <label for="questionTitle" class="mb-2">Titre de la question</label>
      <div class="col-12">
        <input
          v-if="isView"
          type="text"
          id="questionTitle"
          :value="question.title"
          class="form form-control"
          placeholder="Titre de la question"
          disabled="disabled"
        />
        <input
          v-else
          type="text"
          id="questionTitle"
          v-model="questionTitle"
          class="form form-control"
          :placeholder="question.title"
          required="required"
        />
      </div>
    </div>
    <div v-if="!isView" class="row my-2">
      <label for="questionImage" class="mb-2">Image illustrant la question</label>
      <div class="col-12">
        <img :src="question.image" width="250" height="200" /><input
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
          v-if="isView"
          type="text"
          id="questionText"
          v-model="question.text"
          class="form form-control"
          placeholder="Texte de la question"
          disabled="disabled"
        />
        <input
          v-else
          type="text"
          id="questionText"
          v-model="questionText"
          class="form form-control"
          :placeholder="question.text"
          required="required"
        />
      </div>
    </div>
    <div v-if="!isView" class="row my-2">
      <label for="questionPosition" class="mb-2">Position de la question</label>
      <div class="col-12">
        <input
          type="number"
          id="questionPosition"
          v-model="questionPosition"
          class="form form-control"
          :placeholder="question.position"
          required="required"
        />
      </div>
    </div>
    <div class="row my-2">
      <label class="mb-2">Réponses proposées</label>
    </div>
    <div
      class="row justify-content-center"
      v-for="(i, index) in question.possibleAnswers"
      v-bind:key="i"
    >
      <div class="row mb-3">
        <div class="col-auto">
          <input
            v-if="isView"
            type="radio"
            v-model="isCorrect"
            disabled="disabled"
            :checked="i.isCorrect"
          />
          <input
            v-else
            type="radio"
            v-model="isCorrect"
            :value="index + 1"
            required="required"
            :checked="i.isCorrect"
          />
        </div>
        <div class="col-lg">
          <input
            v-if="isView"
            type="text"
            class="form-control w-100"
            :value="i.text"
            disabled="disabled"
          />
          <input
            v-else
            type="text"
            class="form-control w-100"
            v-model="answers[i]"
            :placeholder="i.text"
          />
        </div>
      </div>
    </div>
    <div v-if="!isView" class="row justify-content-end my-2">
      <div class="col-4 text-end me-2">
        <button class="btn btn-primary main-btn me-3" @click="submitForm">Sauvegarder</button>
        <router-link to="/admin" class="btn btn-primary main-btn">Annuler</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import QuizApiService from '../services/QuizApiService'
import Swal from 'sweetalert2'

export default {
  name: 'QuestionDisplayView',
  props: ['mode'],
  data() {
    return {
      question: [],
      isView: this.mode === 'view',
      questionTitle: '',
      questionText: '',
      questionPosition: '',
      questionImage: '',
      isCorrect: 0,
      answers: []
    }
  },
  async created() {
    let question = await QuizApiService.getQuestionById(this.$route.params.id)
    this.question = question.data
    this.questionTitle = this.question.title
    this.questionText = this.question.text
    this.questionPosition = this.question.position
    this.answers = this.question.possibleAnswers
  },
  methods: {
    handleDeleteClick() {
      Swal.fire({
        title: 'Voulez-vous supprimer cette question ?',
        showDenyButton: true,
        confirmButtonText: 'Oui',
        denyButtonText: 'Non'
      }).then((result) => {
        if (result.isConfirmed) {
          QuizApiService.deleteQuestion(this.question.id).then((result) => {
            if (result.status === 204) {
              Swal.fire('Supprimé !', '', 'success').then(() => {
                this.$router.push('/admin')
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
    },
    handleEditClick() {
      window.location = '/admin/edit-question/' + this.question.id
    },
    handleImage(e) {
      const selectedImage = e.target.files[0]
      this.createBase64Image(selectedImage)
    },
    createBase64Image(image) {
      const reader = new FileReader()
      reader.onload = (e) => {
        this.question.image = 'data:image/png;base64,' + btoa(e.target.result)
      }
      reader.readAsBinaryString(image)
    },
    async submitForm() {
      let formatedAnswers = []
      let index = 1
      console.log(this.isCorrect)

      this.answers.forEach((element) => {
        formatedAnswers.push({
          text: element.text,
          isCorrect: index == this.isCorrect ? 1 : 0
        })
        index++
      })

      let putResponse = await QuizApiService.updateQuestion(
        this.question.id,
        this.questionTitle,
        this.questionImage,
        this.questionText,
        this.questionPosition,
        formatedAnswers
      )
      console.log(putResponse)

      if (putResponse.status === 204) {
        Swal.fire('Modifié !', '', 'success').then((result) => {
          if (result.isConfirmed) {
            this.$router.push('/admin')
          }
        })
      } else if (putResponse.status === 401) {
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
