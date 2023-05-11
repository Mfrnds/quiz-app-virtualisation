<template>
    <div class="row text-center">
      <h3 class="main-title">{{ question.questionTitle}}</h3>
    </div>
    <div class="row text-center my-3 question-image" :style="{ 'background-image': 'url(' + question.questionImage + ')'}"></div>
    <div class="row text-center my-4">
      <h5>{{ question.questionText }}</h5>
    </div>
    <div class="row justify-content-center">
      <button type="button" class="col-5 mx-2 btn btn-primary main-btn my-2" @click="$emit('answer-selected', i+1)" v-for="(answer, i) in question.possibleAnswers" v-bind:key="answer.date">
          {{ answer.text }}
      </button>
    </div>
    <div class="row">

    </div>
    
</template>

<script>

export default {
  name: "QuestionDisplay",
  props: {
  question: {
    type: Object
  },
  emits: ["answer-selected"]
}
};
</script>
