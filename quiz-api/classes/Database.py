import sqlite3

class Database:
    def __init__(self):
        self.db_connection = sqlite3.connect("quiz.db")
        self.db_connection.isolation_level = None

        # self.db_init()

    def __del__(self):
        self.db_connection.close()

    def execute_sql(self, query, params):
        try:
            cur = self.db_connection.cursor()
            cur.execute("begin")

            cur.execute(query, params)

            cur.execute("commit")
            cur.close()

            return cur.lastrowid

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
            )
        """)