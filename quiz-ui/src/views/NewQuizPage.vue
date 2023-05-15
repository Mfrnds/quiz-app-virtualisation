<template>
  <audio id="audio">
    <source :src="audioFile" type="audio/mpeg">
  </audio>
  <div class="container">
    <div class="row main-container">
      <div class="offset-3 col-6">
        <div class="row text-center mb-2">
          <h1 class="main-title" style="font-size: 4.5rem;">Prêt à jouer ?</h1>
        </div>
        <div class="row justify-content-center text-center my-4">
          <div class="d-grid gap-2 col-6">
            <input type="text" class="form-control" v-model="username" placeholder="Nom d'utilisateur" aria-label="Nom d'utilisateur">
          </div>
        </div>
        <div class="row justify-content-center text-center my-4">
          <div class="d-grid gap-2 col-6">
            <button type="button" class="btn btn-primary btn-lg main-btn" @click="launchNewQuiz">Commencer</button>
          </div>
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
