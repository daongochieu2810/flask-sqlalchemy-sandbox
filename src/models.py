from sqlalchemy import create_engine
from sqlalchemy.sql import text
import os

class Models:
    def __init__(self):
        self.engine = create_engine(os.environ.get('DB_URL', 'postgresql://hieu:hieu@localhost:5432/bt5110'))

    def executeRawSql(self, statement, params={}):
        out = None
        with self.engine.connect() as con:
            out = con.execute(text(statement), params)
        return out

    # data = ( { "id": 1, "title": "The Hobbit", "primary_author": "Tolkien" },
    #              { "id": 2, "title": "The Silmarillion", "primary_author": "Tolkien" },
    #     )

    # statement = text("""INSERT INTO book(id, title, primary_author) VALUES(:id, :title, :primary_author)""")
    def addProfessor(self, value):
        return self.executeRawSql("""INSERT INTO professor (email, password) VALUES(:email, :password);""", value)

    def addBook(self, value):
        # value has the form { "isbn": 2, "title": "The Silmarillion", "author": "Tolkien" }
        return self.executeRawSql("""INSERT INTO book(isbn, title, author) VALUES(:isbn, :title, :author);""", value)

    def updateAssignment(self, value):
        return self.executeRawSql("""UPDATE assignment SET email=:email WHERE isbn=:isbn;""", value)
    
    def addAssignment(self, value):
        return self.executeRawSql("""INSERT INTO assignment(email, isbn) VALUES(:email, :isbn);""", value)

    def getAllAssignments(self):
        return self.executeRawSql("SELECT * FROM assignment;").mappings().all()

    def deleteAssignment(self, value):
        return self.executeRawSql("DELETE FROM assignment where email=:email and isbn=:isbn;", value)

    def getAssignment(self, value):
        values = self.executeRawSql("""SELECT * FROM assignment WHERE email=:email and isbn=:isbn;""", value).mappings().all()
        if len(values) == 0:
            raise Exception("Book {} has not been assignment by {}".format(value["isbn"], value["email"]))
        return values[0]

    def getAllBooks(self):
        return self.executeRawSql("SELECT * FROM book;").mappings().all()

    def getAllUsers(self):
        return self.executeRawSql("SELECT * FROM student;").mappings().all()

    def getBooksAndAssignments(self):
        return self.executeRawSql("SELECT book.isbn, email, title, author FROM book LEFT JOIN assignment ON book.isbn = assignment.isbn;").mappings().all()

    def getProfessorByEmail(self, email):
        values = self.executeRawSql("""SELECT * FROM professor WHERE email=:email;""", {"email": email}).mappings().all()
        if len(values) == 0:
            raise Exception("Professor {} does not exist".format(email))
        return values[0]

    def getStudentByEmail(self, email):
        values = self.executeRawSql("""SELECT * FROM student WHERE email=:email;""", {"email": email}).mappings().all()
        if len(values) == 0:
            raise Exception("Student {} does not exist".format(email))
        return values[0]

    def createModels(self):
        self.executeRawSql(
        """CREATE TABLE IF NOT EXISTS student (
            email TEXT PRIMARY KEY
        );
        """)

        self.executeRawSql(
        """CREATE TABLE IF NOT EXISTS professor (
            email TEXT PRIMARY KEY,
            password TEXT NOT NULL
        );
        """)

        self.executeRawSql(
            """CREATE TABLE IF NOT EXISTS book (
                isbn TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL
            );
            """)

        self.executeRawSql(
            """CREATE TABLE IF NOT EXISTS assignment (
                email TEXT REFERENCES student,
                isbn TEXT REFERENCES book,
                PRIMARY KEY (isbn, email)
            );
            """)
