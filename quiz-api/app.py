from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt_utils, hashlib
from classes.Question import Question, QuestionEncoder
from classes.Database import Database

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
	data = request.get_json()

	question = Question(data["title"], data["text"], data["image"], data["position"])

	# Save in database and return id with code 200
	return {"id": question.persist(data["possibleAnswers"])}, 200

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
	
@app.route('/questions/<int:questionId>', methods=['DELETE'])
def DeleteQuestion(questionId):
	if not CheckIfLogged():
		return 'Unauthorized', 401
	
	db = Database()
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
		# get all questions which position are higher or equal than given position
		c = db.execute_sql("SELECT * FROM Question WHERE position >= ?", (payload["position"],))
		have_to_modify_questions = c.fetchall()
		c.execute("commit")
		c.close()

		for question in reversed(have_to_modify_questions): # decale position from end (easier)
			c = db.execute_sql("UPDATE Question SET position=? WHERE id = ?", (question[4]+1,question[0]))
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
		if (answer_index < len(have_to_modify_answers)-1): # update the number of answers given
			c = db.execute_sql("UPDATE Answer SET text=?, isCorrect=? WHERE id = ?", (payload["possibleAnswers"][answer_index]["text"], (True if payload["possibleAnswers"][answer_index]["isCorrect"] == 1 else 0) ,answer_to_modify[0]))
			c.execute("commit")
			c.close()
			answer_index += 1
		else: # else we delete registered answer.
			c = db.execute_sql("DELETE FROM Answer WHERE id = ?", (answer_to_modify[0],))
			c.execute("commit")
			c.close()

	return 'No Content', 204

if __name__ == "__main__":
    app.run()