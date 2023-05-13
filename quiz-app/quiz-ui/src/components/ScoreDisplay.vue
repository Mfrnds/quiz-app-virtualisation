<template>
  <ul class="list-group" style="max-height: 230px; overflow: scroll">
    <li class="list-group-item" v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
      {{ scoreEntry.playerName }} - {{ scoreEntry.score }} points
      <span
        v-if="scoreEntry.playerName == playerName && scoreEntry.score == score"
        class="badge text-bg-success"
        >TOI</span
      >
    </li>
  </ul>
</template>

<script>
import quizApiService from '@/services/QuizApiService'
import participationsStorageService from '../services/ParticipationStorageService'

export default {
  name: 'ScoreDisplay',
  data() {
    return {
      registeredScores: [],
      playerName: participationsStorageService.getPlayerName(),
      score: participationsStorageService.getParticipationScore()
    }
  },
  async created() {
    let quizInfo = await quizApiService.getQuizInfo()

    this.registeredScores = quizInfo.data.scores
    console.log(this.playerName)
    console.log(this.score)
  }
}
</script>
