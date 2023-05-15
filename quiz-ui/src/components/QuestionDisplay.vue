<template>
  <div class="row text-center my-2">
    <h3 class="main-title">{{ question.questionTitle }}</h3>
  </div>
  <div class="row text-center mt-3 mb-4 question-image">
    <div
      class="div"
      :style="{
        'background-position': 'center',
        'background-size': 'contain',
        'background-repeat': 'no-repeat',
        'background-image': 'url(' + question.questionImage + ')'
      }"
    ></div>
  </div>
  <div class="row text-center mt-4 mb-5">
    <h5>{{ question.questionText }}</h5>
  </div>
  <div class="row justify-content-center">
    <button
      type="button"
      class="col-5 mx-2 btn btn-primary main-btn my-2"
      @click="$emit('answer-selected', i + 1)"
      v-for="(answer, i) in question.possibleAnswers"
      v-bind:key="answer.date"
    >
      {{ answer.text }}
    </button>
  </div>
  <div class="row"></div>
</template>

<script>
export default {
  name: 'QuestionDisplay',
  props: {
    question: {
      type: Object
    },
    emits: ['answer-selected']
  }
}
</script>
