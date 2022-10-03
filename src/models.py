from sqlalchemy import create_engine
from sqlalchemy.sql import text
import os

class Models:
    def __init__(self):
        self.engine = create_engine(os.getenv('DATABASE_URL', 'postgresql://hieu:hieu@localhost:5432/bt5110'))

    def executeRawSql(self, statement, params={}):
        out = None
        with self.engine.connect() as con:
            out = con.execute(text(statement), params)
        return out

    # data = ( { "id": 1, "title": "The Hobbit", "primary_author": "Tolkien" },
    #              { "id": 2, "title": "The Silmarillion", "primary_author": "Tolkien" },
    #     )

    # statement = text("""INSERT INTO book(id, title, primary_author) VALUES(:id, :title, :primary_author)""")
    def addUser(self, value):
        return self.executeRawSql("""INSERT INTO account(email, password) VALUES(:email, :password);""", value)

    def addBook(self, value):
        # value has the form { "isbn": 2, "title": "The Silmarillion", "author": "Tolkien" }
        return self.executeRawSql("""INSERT INTO book(isbn, title, author) VALUES(:isbn, :title, :author);""", value)

    def updateReader(self, value):
        return self.executeRawSql("""UPDATE read SET email=:email WHERE isbn=:isbn;""", value)
    
    def addReader(self, value):
        return self.executeRawSql("""INSERT INTO read(email, isbn) VALUES(:email, :isbn);""", value)

    def getAllReads(self):
        return self.executeRawSql("SELECT * FROM read;").mappings().all()

    def deleteRead(self, value):
        return self.executeRawSql("DELETE FROM read where email=:email and isbn=:isbn;", value)

    def getRead(self, value):
        values = self.executeRawSql("""SELECT * FROM read WHERE email=:email and isbn=:isbn;""", value).mappings().all()
        if len(values) == 0:
            return "Book {} has not been read by {}".format(value["isbn"], value["email"])
        return values[0]

    def getAllBooks(self):
        return self.executeRawSql("SELECT * FROM book;").mappings().all()

    def getAllUsers(self):
        return self.executeRawSql("SELECT * FROM account;").mappings().all()

    def getBookAndReads(self):
        return self.executeRawSql("SELECT book.isbn, email, title, author FROM book LEFT JOIN read ON book.isbn = read.isbn;").mappings().all()

    def getUserByEmail(self, email):
        values = self.executeRawSql("""SELECT * FROM account WHERE email=:email;""", {"email": email}).mappings().all()
        if len(values) == 0:
            return "User {} does not exist".format(email)
        return values[0]

    def createModels(self):
        self.executeRawSql(
        """CREATE TABLE IF NOT EXISTS account (
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
            """CREATE TABLE IF NOT EXISTS read(
                email TEXT REFERENCES account,
                isbn TEXT REFERENCES book,
                PRIMARY KEY (isbn, email)
            );
            """)
