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
	return {"id": question.persist()}, 200
	
@app.route('/questions/<int:questionId>', methods=['GET'])
def GetQuestion(questionId):
	db = Database()
	c = db.execute_sql("SELECT * FROM Question WHERE id = ?", (questionId,))
	question = c.fetchone()
	c.close()

	if question:
		return jsonify({
			'id': question[0],
			'title': question[1],
			'position': question[4],
			'text': question[2],
			'image': question[3],
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



if __name__ == "__main__":
    app.run()