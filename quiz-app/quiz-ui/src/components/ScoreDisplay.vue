<template>
  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }} points
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
name: "ScoreDisplay",
data() {
    return {
      registeredScores: []
    };
  },
  async created() {
    let quizInfo = await quizApiService.getQuizInfo();

    this.registeredScores = quizInfo.data.scores;
  }
};
</script>
