import axios from 'axios'
import AdminService from './AdminService'

const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
})

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      'Content-Type': 'application/json'
    }
    if (token != null) {
      headers.authorization = 'Bearer ' + token
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data
    })
      .then((response) => {
        return { status: response.status, data: response.data }
      })
      .catch((error) => {
        console.error(error)
      })
  },
  getQuizInfo() {
    return this.call('get', 'quiz-info')
  },
  getQuestionById(id) {
    return this.call('get', 'questions/' + id)
  },
  getQuestionByPosition(position) {
    return this.call('get', 'questions?position=' + position)
  },
  postAnswers(playerName, answers) {
    return this.call('post', 'participations', { playerName: playerName, answers: answers })
  },
  postNewQuestion(title, image, text, position, answers){
    return this.call('post', 'questions', { title: title, text:text, image: image, position:position,  possibleAnswers: answers }, AdminService.getToken())
  },
  postLogin(password) {
    return this.call('post', 'login', { password: password })
  }
}
