from classes.Database import Database
from json import JSONEncoder

# Exemple de création de classe en python
class Question():
    def __init__(self, title: str, text: str, image: str, position: int):
        self.title = title
        self.text = text
        self.image = image
        self.position = position

    def persist(self):
        db = Database()
        c = db.execute_sql("INSERT INTO Question (title,text,image,position) VALUES (?, ?, ?, ?);", (self.title, self.text, self.image, self.position))
        lastrowid = c.lastrowid
        c.execute("commit")
        c.close()
        return lastrowid

class QuestionEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__