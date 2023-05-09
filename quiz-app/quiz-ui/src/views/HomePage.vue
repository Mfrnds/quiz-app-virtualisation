<template>
  <div class="container">
    <div class="row main-container">
      <div class="offset-4 col-4">
        <div class="row text-center">
          <h1 class="main-title">Harry Potter Quiz</h1>
        </div>
        <div class="row text-center">
          <router-link to="/start-new-quiz-page"><button type="button" class="btn btn-primary main-btn">Participer</button></router-link>
        </div>
        <div class="row text-center my-4">
          <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
            {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
          </div>
        </div>
      </div>
    </div>
  </div>  
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: [],
      size: 0,
    };
  },
  async created() {
    let quizInfo = await quizApiService.getQuizInfo();

    this.registeredScores = quizInfo.data.scores;
    this.size = quizInfo.data.size;
  }
};
</script>