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
          <ScoreDisplay/>
        </div>
      </div>
    </div>
  </div>  
</template>

<script>
import ScoreDisplay from '../components/ScoreDisplay.vue';


export default {
    name: "HomePage",
    components: { ScoreDisplay }
};
</script>