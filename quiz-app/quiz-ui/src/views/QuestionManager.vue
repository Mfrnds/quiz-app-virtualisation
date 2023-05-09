<template>
  <div class="container">
    <div class="row main-container">
      <div class="col-12">
        <div class="row text-center">
          <div class="col-6">
            <h2 class="main-title">Q° {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h2>
          </div>
        </div>
        <div class="row text-center">
          <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
        </div>
      </div>
    </div>
  </div>  
</template>

<script>
import participationStorageService from "../services/ParticipationStorageService";
import quizApiService from "../services/QuizApiService";
import QuestionDisplay from "../components/QuestionDisplay.vue";

export default {
  name: "QuestionManager",
  data(){
    return{
      currentQuestion:{
        questionTitle: '',
        questionText: '',
        questionImage: '',
        possibleAnswers: []
      },
      currentQuestionPosition : 1,
      selectedAnswers: []
    }
  },
  components: {
    QuestionDisplay
  },
  async created() {
     this.loadQuestionByPosition()
  },
  methods:{
    async loadQuestionByPosition(){
      let data = await quizApiService.getQuestion(this.currentQuestionPosition);
      const question = data.data;

      this.currentQuestion.questionTitle = question.title;
      this.currentQuestion.questionText = question.text; 
      this.currentQuestion.questionImage = question.image;
      this.currentQuestion.possibleAnswers = question.possibleAnswers;
    },
    async answerClickedHandler(answerId){
      this.currentQuestionPosition += 1;
      await this.loadQuestionByPosition();
      this.selectedAnswers.push(answerId)
    },
    async endQuiz(){
      
    }
  }
};
</script>
