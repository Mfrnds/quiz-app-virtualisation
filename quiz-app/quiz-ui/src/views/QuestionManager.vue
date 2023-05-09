<template>
  <div class="container">
    <div class="row main-container">
      <div class="offset-4 col-4">
        <div class="row text-center">
          <div class="col-6">
            <h2 class="main-title">Q° {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h2>
          </div>
        </div>
        <div class="row text-center">
          <QuestionDisplay :question="currentQuestion" @click-on-answer="answerClickedHandler" />
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
      currentQuestionPosition : 0,
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
      let question = await quizApiService.getQuestion(this.currentQuestionPosition);

      this.currentQuestion.questionTitle = question.title;
      this.currentQuestion.questionText = question.text; 
      this.currentQuestion.questionImage = question.image;
      this.currentQuestion.possibleAnswers = question.possibleAnswers;
    },
    answerClickedHandler(payload){
      console.log(payload);
      this.currentQuestionPosition += 1;
      this.loadQuestionByPosition();
      // this.selectedAnswers.push()
    },
    endQuiz(){
      
    }
  }
};
</script>
