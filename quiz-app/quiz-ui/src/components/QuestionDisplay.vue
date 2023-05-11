<template>
    <div class="row text-center">
      <h1 class="main-title">{{ question.questionTitle}}</h1>
    </div>
    <div class="row text-center my-2">
      <img width="500" height="250" v-if="question.questionImage" :src="question.questionImage" />
    </div>
    <div class="row text-center my-3">
      <h5>{{ question.questionText }}</h5>
    </div>
    <div class="row justify-content-center" v-for="(answer, i) in question.possibleAnswers" v-bind:key="answer.date">
        <button type="button" class="col-4 btn btn-primary main-btn my-2" @click="$emit('answer-selected', i+1)">{{ answer.text }}</button>
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
