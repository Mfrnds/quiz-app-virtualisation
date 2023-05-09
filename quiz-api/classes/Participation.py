from classes.Database import Database
from datetime import datetime

class Participation():
    def __init__(self, playerName: str, score: int):
        self.playerName = playerName
        self.score = score

    def persist(self):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")

        db = Database()
        c = db.execute_sql("INSERT INTO Participation (playerName,score,date) VALUES (?, ?, ?);", (self.playerName, self.score, date_time))
        lastrowid = c.lastrowid
        c.execute("commit")
        c.close()
        return lastrowid
