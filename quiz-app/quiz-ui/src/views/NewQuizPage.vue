<template>
  <div class="container">
    <div class="row main-container">
      <div class="offset-4 col-4">
        <div class="row text-center">
          <h1 class="main-title">Prêt à jouer ?</h1>
        </div>
        <div class="row text-center">
          <div class="input-group mb-3">
            <input type="text" class="form-control" v-model="username" placeholder="Nom d'utilisateur" aria-label="Nom d'utilisateur">
          </div>
        </div>
        <div class="row text-center">
          <button type="button" class="btn btn-primary main-btn" @click="launchNewQuiz">Commencer</button>
        </div>
      </div>
    </div>
  </div>  
</template>

<script>
import participationStorageService from "@/ParticipationStorageService";

export default {
  name: "NewQuizPage",
  data() {
    return {
      username: ''
    };
  },
  methods:{
    launchNewQuiz(){
      participationStorageService.savePlayerName(this.username);
      this.$router.push('/questions');
    },
  }
};
</script>
