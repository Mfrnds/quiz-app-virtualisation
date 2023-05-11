<template>
    <div class="container">
      <div class="row main-container">
        <div class="col-12">
          <div class="row">
            <QuestionDisplayView />
          </div>
        </div>
      </div>
    </div>  
  </template>
  
  <script>
import QuestionDisplayView from "../components/QuestionDisplayView.vue";
  
  export default {
    name: "QuestionViewPage",
    components: {
    QuestionDisplayView
}
  };
  </script>
  