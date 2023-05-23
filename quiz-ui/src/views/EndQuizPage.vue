<template>
  <div class="container">
    <div class="row main-container">
      <div class="offset-3 col-6">
        <div class="row text-center mb-2">
          <h1 class="main-title" style="font-size: 4.5rem;">Quiz terminé !</h1>
        </div>
        <div class="row justify-content-center text-center my-4">
          <div class="d-grid gap-2 col-6">
            <button type="button" class="btn btn-primary btn-lg main-btn"><router-link to="/">Accueil</router-link></button>
          </div>
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