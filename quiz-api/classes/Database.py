import sqlite3

class Database:
    def __init__(self):
        self.db_connection = sqlite3.connect("quiz.db")
        self.db_connection.isolation_level = None

        # self.db_init()

    def __del__(self):
        self.db_connection.close()

    def getConnection(self):
        return self.db_connection

    def execute_sql(self, query, params):
        try:
            cur = self.db_connection.cursor()
            cur.execute("begin")

            cur.execute(query, params)

            return cur

        except:
            cur.execute("rollback")
            cur.close()
            raise
        
    def db_init(self):
        self.execute_sql("""
            CREATE TABLE "Question" (
                "id"	INTEGER NOT NULL UNIQUE,
                "title"	TEXT NOT NULL,
                "text"	TEXT NOT NULL,
                "image"	BLOB,
                "position"	INTEGER,
                PRIMARY KEY("id" AUTOINCREMENT)
            );
            CREATE TABLE "Answer" (
                "id"	INTEGER UNIQUE,
                "text"	TEXT NOT NULL,
                "isCorrect"	INTEGER NOT NULL,
                "question_id"	INTEGER NOT NULL,
                PRIMARY KEY("id" AUTOINCREMENT),
                FOREIGN KEY("question_id") REFERENCES "Question"("id")
            );
        """)