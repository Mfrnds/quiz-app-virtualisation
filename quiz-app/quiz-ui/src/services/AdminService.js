export default {
    clear() {
      window.localStorage.clear()
    },
    saveToken(token) {
      window.localStorage.setItem('token', token)
    },
    getToken() {
      return window.localStorage.getItem('token')
    }
  }
  