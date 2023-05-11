<template>
    <div class="main-container pt-4">
        <div class="row text-center">
            <h1 class="main-title">Visualisation d'une question</h1>
            <hr>
        </div>
        <div class="row my-2">
            <label for="questionTitle" class="mb-2">Titre de la question</label>
            <div class="col-12"><input type="text" id="questionTitle" :value="question.title" class="form form-control" placeholder="Titre de la question" disabled="disabled"></div>
        </div>
        <div class="row my-2">
            <label for="questionImage" class="mb-2">Image illustrant la question</label>
            <div class="col-12"><center><img :src="question.image"></center></div>
        </div>
        <div class="row my-2">
            <label for="questionText" class="mb-2">Intitulé de la question</label>
            <div class="col-12"><input type="text" id="questionText" v-model="question.text" class="form form-control" placeholder="Texte de la question" disabled="disabled"></div>
        </div>
        <div class="row my-2">
            <label for="questionPosition" class="mb-2">Position de la question</label>
            <div class="col-12"><input type="number" id="questionPosition" v-model="question.position" class="form form-control" placeholder="Position de la question" disabled="disabled"></div>
        </div>
        <div class="row my-2">
            <label class="mb-2">Réponses proposées</label>
        </div>
        <div class="row justify-content-center" v-for="i in question.possibleAnswers">
            <div class="row mb-3">
                <div class="col-auto">
                    <input type="radio" v-model="isCorrect" disabled="disabled" :checked="i.isCorrect == 1 ? true : false">
                </div>
                <div class="col-lg">
                    <input type="text" class="form-control w-100" :value="i.text" disabled="disabled">
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import QuizApiService from '../services/QuizApiService';

export default {
  name: "QuestionDisplayCreation",
  data() {
    return {
      question: []
    };
  },
  async created() {
    let question = await QuizApiService.getQuestionById(this.$route.params.id);
    this.question = question.data;
    console.log(question.data)
  }
};
</script>
