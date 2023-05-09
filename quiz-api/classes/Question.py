from classes.Database import Database

# Exemple de création de classe en python
class Question():
    def __init__(self, title: str, text: str, image: str, position: int):
        self.title = title
        self.text = text
        self.image = image
        self.position = position

    def persist(self, answers):
        db = Database()
        c = db.execute_sql("INSERT INTO Question (title,text,image,position) VALUES (?, ?, ?, ?);", (self.title, self.text, self.image, self.position))
        lastrowid = c.lastrowid
        c.execute("commit")

        for answer in answers:
            c = db.execute_sql("INSERT INTO Answer (text,isCorrect,question_id) VALUES (?, ?, ?);", (answer["text"], (1 if answer["isCorrect"] else 0), lastrowid))
            c.execute("commit")

        c.close()
        return lastrowid
