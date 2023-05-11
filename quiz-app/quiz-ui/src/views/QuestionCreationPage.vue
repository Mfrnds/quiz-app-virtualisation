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
import QuestionDisplayCreation from "../components/QuestionDisplayCreation.vue";

export default {
  name: "QuestionCreationPage",
  components: {
    QuestionDisplayCreation
  }
};
</script>
