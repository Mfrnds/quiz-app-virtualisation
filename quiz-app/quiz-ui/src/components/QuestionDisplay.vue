<template>
    <div class="row text-center">
      <h1 class="main-title">{{ question.questionTitle}}</h1>
    </div>
    <div class="row text-center">
      <img width="500px" height="250px" v-if="question.questionImage" :src="question.questionImage" />
    </div>
    <div class="row text-center">
      <h5>{{ question.questionText }}</h5>
    </div>
    <div class="row text-center">
      <div v-for="answer in question.possibleAnswers" v-bind:key="answer.date">
        <button type="button" class="btn btn-primary main-btn my-2" @click="$emit('answer-selected', answer.id)">{{ answer.text }}</button>
      </div>
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
