<template>
  <h1>Home page</h1>
  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
  <router-link to="/start-new-quiz-page">Démarrer le quiz !</router-link>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

let registeredScores = [];

export default {
  name: "HomePage",
  data() {
    return {
    };
  },
  async created() {
    let test = await quizApiService.getQuizInfo();

		console.log(test);
  }
};
</script>