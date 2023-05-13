<template>
  <div class="container">
    <div class="row main-container">
      <div class="col-12">
        <div class="row">
          <QuestionDisplayView :mode="mode" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import QuestionDisplayView from '../components/QuestionDisplayView.vue'

export default {
  name: 'QuestionViewPage',
  props: ['mode'],
  components: {
    QuestionDisplayView
  }
}
</script>
