<template>
  <audio id ="audio" autoplay>
    <source :src="audioFile" type="audio/mpeg">
  </audio>
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