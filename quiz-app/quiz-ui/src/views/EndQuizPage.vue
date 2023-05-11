<template>
  <div class="container">
    <div class="row main-container">
      <div class="offset-4 col-4">
        <div class="row text-center">
          <h1 class="main-title">Quiz terminé !</h1>
        </div>
        <div class="row text-center">
          <router-link to="/"><button type="button" class="btn btn-primary main-btn">Retour accueil</button></router-link>
        </div>
        <div class="row text-center my-4">
          <span class="main-title">Classement</span>
        </div>
        <div class="row text-center my-4">
          <ScoreDisplay/>
        </div>
      </div>
    </div>
  </div>  
</template>

<script>
import ScoreDisplay from "../components/ScoreDisplay.vue";

export default {
    name: "EndQuizPage",
    data() {
        return {
            registeredScores: []
        };
    },
    async created() {
    },
    components: { ScoreDisplay }
};
</script>