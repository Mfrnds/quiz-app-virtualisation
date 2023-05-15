<template>
  <audio id="audio" autoplay>
    <source :src="audioFile" type="audio/mpeg" />
  </audio>
  <div class="container">
    <div class="row main-container">
      <div class="offset-3 col-6">
        <div class="row text-center mb-2">
          <h1 class="main-title" style="font-size: 4.5rem">Connexion</h1>
        </div>
        <div class="row justify-content-center my-4">
          <div class="card" style="width: 25rem">
            <div class="card-body">
              <form v-on:submit.prevent="handleSubmit">
                <div class="row alert alert-danger" :class="{ 'd-none': isCorrect }" role="alert">
                  <span class="ps-0">Identifiants incorrects</span>
                </div>
                <div class="row mb-3">
                  <label for="passwordInput" class="form-label">Mot de passe</label>
                  <input
                    type="password"
                    v-model="password"
                    class="form-control"
                    id="passwordInput"
                    required
                  />
                </div>
                <div class="row justify-content-center">
                  <button type="submit" class="col-4 btn btn-primary main-btn">Connexion</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import quizApiService from '../services/QuizApiService'
import adminService from '../services/AdminService'

export default {
  name: 'LoginPage',
  data() {
    return {
      isCorrect: true,
      password: ''
    }
  },
  methods: {
    async handleSubmit() {
      let loginData = await quizApiService.postLogin(this.password)

      if (loginData.status === 200) {
        adminService.saveToken(loginData.data.token)
        this.$router.push('admin')
      } else if (loginData.status === 401) {
        this.isCorrect = false
      }
    }
  }
}
</script>
