<template>
    <div class="row text-center">
      <h1 class="main-title">{{ question.questionTitle}}</h1>
    </div>
    <div class="row text-center">
      <img v-if="question.questionImage" :src="question.questionImage" />
    </div>
    <div class="row text-center">
      <h5>{{ question.questionText }}</h5>
    </div>
    <div class="row text-center">
      <div v-for="answer in question.possibleAnswers" v-bind:key="answer.date">
        <div class="form-check" @click="$emit('answer-selected', answer.id)">
          <input class="form-check-input" type="radio" name="radio-answer" id="radio-answer-{{ answer.id }}">
          <label class="form-check-label" for="radio-answer">
            {{answer.text}}
          </label>
        </div>
      </div>
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
