<template>
  <div class="container">
    <div class="row main-container">
      <div class="col-12">
        <div class="row">
          <QuestionDisplayCreation />
        </div>
      </div>
    </div>
  </div>  
</template>

<script>
import participationStorageService from "../services/ParticipationStorageService";
import quizApiService from "../services/QuizApiService";
import QuestionDisplayCreation from "../components/QuestionDisplayCreation.vue";

export default {
  name: "QuestionCreationManager",
  components: {
    QuestionDisplayCreation
  }
};
</script>
