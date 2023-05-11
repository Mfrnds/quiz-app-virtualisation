<template>
  <audio id ="audio" autoplay>
    <source :src="audioFile" type="audio/mpeg">
  </audio>
  <div class="container">
    <div class="row main-container">
      <div class="offset-3 col-6">
        <div class="row text-center mb-2">
          <h1 class="main-title" style="font-size: 4.5rem;">Harry Potter Quiz</h1>
        </div>
        <div class="row justify-content-center text-center my-4">
          <div class="d-grid gap-2 col-6">
            <router-link  class="btn btn-primary btn-lg main-btn" to="/start-new-quiz-page">Participer</router-link>
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
import ScoreDisplay from '../components/ScoreDisplay.vue';
import audioFile from "@/assets/audio.mp3";

export default {
  name: "HomePage",
  components: { ScoreDisplay },
  data() {
    return {
      audioFile: audioFile,
    };
  },
  methods: {
    savePosition() {
      const audio = document.getElementById("audio");
      localStorage.setItem("audioPosition", audio.currentTime);
    }
  },

  mounted() {
    const audio = document.getElementById("audio");
    audio.loop = true;
    audio.currentTime = 0;

    document.body.addEventListener('click', () => {
      audio.play();
    }, { once: true });
  },

  beforeRouteLeave(){
    this.savePosition()
  }

};
</script>