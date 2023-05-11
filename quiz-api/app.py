from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt_utils, hashlib
from classes.Question import Question
from classes.Database import Database
from classes.Participation import Participation

app = Flask(__name__)
CORS(app)

# Function to check if user is logged (as admin obviously)
def CheckIfLogged():
	if "Authorization" in request.headers:
		#Récupérer le token envoyé en paramètre
		sub = jwt_utils.decode_token(request.headers["Authorization"].split("Bearer ")[1])
		if sub != "quiz-app-admin":
			return False
		return True
	return False

# REBUILD DATABASE
@app.route('/rebuild-db', methods=['POST'])
def RebuildDatabase():
	db = Database()
	db.db_init()

	
	return 'Ok', 200

# AUTHENTICATION

@app.route('/login', methods=['POST'])
def Login():
	payload = request.get_json()
	tried_password = payload["password"].encode('UTF-8')

	if (hashlib.md5(tried_password).digest() == b'\x192\xe8\xf1c]\x93\xb6\x8a+\xf7\xdc\x07\xa4\x0e\xc1'):
		token = jwt_utils.build_token()
		return {"token":token}, 200
	
	return 'Unauthorized', 401

# QUESTIONS

@app.route('/questions', methods=['POST'])
def CreateQuestion():
	if not CheckIfLogged():
		return 'Unauthorized', 401

	#récupèrer un l'objet json envoyé dans le body de la requète
	payload = request.get_json()
	db = Database()

	c = db.execute_sql("SELECT * FROM Question WHERE position = ?", (payload["position"],))
	position_question = c.fetchone()
	c.execute("commit")
	c.close()
	
	if position_question: # then we have to decale all questions
		# get all questions which position are higher or equal than given position and lower than current pos
		if (payload["position"] < position_question[4]):
			c = db.execute_sql("SELECT * FROM Question WHERE position >= ? AND position <= ?", (payload["position"],position_question[4]))
			increment = 1
		else:
			c = db.execute_sql("SELECT * FROM Question WHERE position >= ? AND position <= ?", (position_question[4],payload["position"]))
			increment = -1

		have_to_modify_questions = c.fetchall()
		c.execute("commit")
		c.close()

		for question in reversed(have_to_modify_questions): # decale position from end (easier)
			c = db.execute_sql("UPDATE Question SET position=? WHERE id = ?", (question[4]+increment,question[0]))
			c.execute("commit")
			c.close()

	question = Question(payload["title"], payload["text"], payload["image"], payload["position"])

	# Save in database and return id with code 200
	return {"id": question.persist(payload["possibleAnswers"])}, 200

@app.route('/questions/all', methods=['GET'])
def GetAllQuestions():
	db = Database()
	c = db.execute_sql("SELECT * FROM Question ", ())
	questions = c.fetchall()
	c.close()
	questions_data = []
	for question in questions:
		questions_data.append({
			"id": question[0],
			"text": question[2],
			"title": question[1]
		})
	return jsonify(questions_data)

@app.route('/questions', methods=['GET'])
def GetQuestionByPosition():
	if not request.args.get('position'):
		return jsonify({'error': 'Question not found'}), 404
	
	db = Database()
	c = db.execute_sql("SELECT * FROM Question JOIN Answer ON Answer.question_id = Question.id WHERE Question.position = ?", (request.args.get('position'),))
	question = c.fetchall()
	c.close()

	answers = []
	for answer in question:
		answers.append({
			"id": answer[5],
			"text": answer[6],
			"isCorrect": False if answer[7] == 0 else True
		})

	if question:
		return jsonify({
			'id': question[0][0],
			'title': question[0][1],
			'position': question[0][4],
			'text': question[0][2],
			'image': question[0][3],
			'possibleAnswers': answers
		})
	else:
		return jsonify({'error': 'Question not found'}), 404
	
@app.route('/questions/<int:questionId>', methods=['GET'])
def GetQuestionById(questionId):
	db = Database()
	c = db.execute_sql("SELECT * FROM Question JOIN Answer ON Answer.question_id = Question.id WHERE Question.id = ?", (questionId,))
	question = c.fetchall()
	c.close()

	answers = []
	for answer in question:
		answers.append({
			"id": answer[5],
			"text": answer[6],
			"isCorrect": False if answer[7] == 0 else True
		})

	if question:
		return jsonify({
			'id': question[0][0],
			'title': question[0][1],
			'position': question[0][4],
			'text': question[0][2],
			'image': question[0][3],
			'possibleAnswers': answers
		})
	else:
		return jsonify({'error': 'Question not found'}), 404
	
@app.route('/questions/all', methods=['DELETE'])
def DeleteAllQuestions():
	if not CheckIfLogged():
		return 'Unauthorized', 401
	
	db = Database()

	# delete all answers
	c = db.execute_sql("DELETE FROM Answer", ())
	c.execute("commit")
	c.close()

	# delete all questions
	c = db.execute_sql("DELETE FROM Question", ())
	c.execute("commit")
	c.close()

	return 'No Content', 204
	
@app.route('/questions/<int:questionId>', methods=['DELETE'])
def DeleteQuestion(questionId):
	if not CheckIfLogged():
		return 'Unauthorized', 401
	
	db = Database()

	# get question that will be deleted
	c = db.execute_sql("SELECT * FROM Question WHERE id=?;", (questionId,))
	question = c.fetchone()
	c.execute("commit")
	c.close()

	# get total questions count
	c = db.execute_sql("SELECT COUNT(*) FROM Question", ())
	count = c.fetchone()[0]
	c.execute("commit")
	c.close()

	# if question to delete isn't the last one then we have to reorder the rest of the question positions by decrementing them
	if (question[4] < count):
		c = db.execute_sql("SELECT * FROM Question WHERE position > ?;", (question[4],))
		questions_to_decrement = c.fetchall()
		c.execute("commit")
		c.close()

		for quest_decr in questions_to_decrement:
			c = db.execute_sql("UPDATE Question SET position=? WHERE id = ?", (quest_decr[4]-1,quest_decr[0])) # decrement each question position
			c.execute("commit")
			c.close()

	c = db.execute_sql("DELETE FROM Question WHERE id = ?", (questionId,))
	c.execute("commit")
	c.close()

	return 'No Content', 204

@app.route('/questions/<int:questionId>', methods=['PUT'])
def UpdateQuestion(questionId):
	if not CheckIfLogged():
		return 'Unauthorized', 401
	
	db = Database()
	payload = request.get_json()

	c = db.execute_sql("SELECT * FROM Question WHERE id = ?", (questionId,))
	question = c.fetchone()
	c.execute("commit")
	c.close()

	if not question:
		return 'Not Found', 404

	c = db.execute_sql("SELECT COUNT(*) FROM Question", ())
	count = c.fetchone()[0]
	c.execute("commit")
	c.close()

	if (payload["position"] > count):
		return 'Position cannot be higher than questions total count', 401
	
	c = db.execute_sql("SELECT * FROM Question WHERE position = ?", (payload["position"],))
	position_question = c.fetchone()
	c.execute("commit")
	c.close()
	
	if position_question: # then we have to decale all questions
		# get all questions which position are higher or equal than given position and lower than current pos
		if (payload["position"] < question[4]):
			c = db.execute_sql("SELECT * FROM Question WHERE position >= ? AND position <= ?", (payload["position"],question[4]))
			increment = 1
		else:
			c = db.execute_sql("SELECT * FROM Question WHERE position >= ? AND position <= ?", (question[4],payload["position"]))
			increment = -1

		have_to_modify_questions = c.fetchall()
		c.execute("commit")
		c.close()

		for question in reversed(have_to_modify_questions): # decale position from end (easier)
			c = db.execute_sql("UPDATE Question SET position=? WHERE id = ?", (question[4]+increment,question[0]))
			c.execute("commit")
			c.close()

	# we can finally update our original question!
	c = db.execute_sql("UPDATE Question SET title=?, text=?, image=?, position=? WHERE id = ?", (payload["title"], payload["text"], payload["image"], payload["position"], questionId))
	c.execute("commit")
	c.close()

	# we can also update answers
	c = db.execute_sql("SELECT * FROM Answer WHERE question_id = ?", (questionId,))
	have_to_modify_answers = c.fetchall()
	c.execute("commit")
	c.close()

	answer_index = 0

	for answer_to_modify in have_to_modify_answers: # modify answers
		if (answer_index <= len(have_to_modify_answers)-1): # update the number of answers given
			c = db.execute_sql("UPDATE Answer SET text=?, isCorrect=? WHERE id = ?", (payload["possibleAnswers"][answer_index]["text"], (True if payload["possibleAnswers"][answer_index]["isCorrect"] == 1 else 0) ,answer_to_modify[0]))
			c.execute("commit")
			c.close()
			answer_index += 1
		else: # else we delete registered answer.
			c = db.execute_sql("DELETE FROM Answer WHERE id = ?", (answer_to_modify[0],))
			c.execute("commit")
			c.close()

	return 'No Content', 204

# QUIZ INFO
@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	db = Database()

	# Get the size field
	c = db.execute_sql("SELECT COUNT(*) FROM Question", ())
	count = c.fetchone()[0]
	c.execute("commit")
	c.close()

	# Get all participations
	c = db.execute_sql("SELECT * FROM Participation ORDER BY score DESC", ())
	rows = c.fetchall()
	c.execute("commit")
	c.close()

	scores = []
	for score in rows:
		scores.append({
			"playerName": score[1],
			"score": score[2],
			"date": score[3]
		})

	return jsonify({
		'size': count,
		'scores': scores
	})
	

# PARTICIPATIONS

@app.route('/participations', methods=['POST'])
def RecordParticipation():
	#récupèrer un l'objet json envoyé dans le body de la requète
	db = Database()
	payload = request.get_json()
	answers = payload["answers"]

	# compute if answers are correct
	# get all questions and correct answer first
	c = db.execute_sql("SELECT q.*, a.*, (SELECT COUNT(*) + 1 FROM Answer a2 WHERE a2.question_id = q.id AND a2.id < a.id) AS answer_index FROM Question q JOIN Answer a ON q.id = a.question_id AND a.isCorrect = 1;", ())
	questions = c.fetchall()
	c.execute("commit")
	c.close()

	index = 0
	score = 0

	if (len(answers) != len(questions)):
		return 'Bad Request', 400 

	for question in questions:
		if (question[9] == answers[index]): # if index of correct answer is equal to what user said then we add a point
			score += 1
		index += 1

	participation = Participation(payload["playerName"], score)

	# Save in database
	participation.persist()

	# return results with code 200
	return {
		"playerName": payload["playerName"],
		"score": score
	}, 200

@app.route('/participations/all', methods=['DELETE'])
def DeleteAllParticipations():
	if not CheckIfLogged():
		return 'Unauthorized', 401

	db = Database()

	# delete all participations
	c = db.execute_sql("DELETE FROM Participation", ())
	c.execute("commit")
	c.close()

	return 'No Content', 204



if __name__ == "__main__":
    app.run()