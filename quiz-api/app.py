from flask import Flask, request
from flask_cors import CORS
import jwt_utils, hashlib
from classes.Question import Question, QuestionEncoder

app = Flask(__name__)
CORS(app)

# Function to check if user is logged (as admin obviously)
def CheckIfLogged():
	if "Authorization" in request.headers:
		#Récupérer le token envoyé en paramètre
		sub = jwt_utils.decode_token(request.headers.get('Authorization'))

		if sub != "quiz-app-admin":
			return 'Unauthorized', 401

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
	# CheckIfLogged()

	#récupèrer un l'objet json envoyé dans le body de la requète
	data = request.get_json()

	question = Question(data["title"], data["text"], data["image"], data["position"])
	# Save in database and return id with code 200
	return {"id": question.persist()}, 200
	

if __name__ == "__main__":
    app.run()