<template>
  <audio id="audio">
    <source :src="audioFile" type="audio/mpeg">
  </audio>
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
import participationStorageService from "../services/ParticipationStorageService";
import audioFile from "@/assets/audio.mp3";

export default {
  name: "NewQuizPage",
  data() {
    return {
      username: "",
      audioFile: audioFile,
    };
  },
  methods: {
    launchNewQuiz() {
      participationStorageService.savePlayerName(this.username);
      this.$router.push("/questions");
    },
    loadPosition() {
      const audio = document.getElementById("audio");
      let currentTime = localStorage.getItem("audioPosition") || 0;
      audio.currentTime = currentTime;
      audio.play()
    },
  },
  mounted() {
    this.loadPosition();
  },
};
</script>
