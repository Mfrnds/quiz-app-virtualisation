export default {
  clear() {
    // todo : implement
  },
  savePlayerName(playerName) {
    window.localStorage.setItem('playerName', playerName)
  },
  getPlayerName() {
    window.localStorage.getItem('playerName')
  },
  saveParticipationScore(participationScore) {
    // todo : implement
  },
  getParticipationScore() {
    // todo : implement
  }
}
