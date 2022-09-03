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

    def updateBorrower(self, value):
        return self.executeRawSql("""UPDATE borrow SET email=:email WHERE isbn=:isbn;""", value)
    
    def addBorrower(self, value):
        return self.executeRawSql("""INSERT INTO borrow(email, isbn) VALUES(:email, :isbn);""", value)

    def getAllBorrows(self):
        return self.executeRawSql("SELECT * FROM borrow;").mappings().all()

    def deleteBorrow(self, value):
        return self.executeRawSql("DELETE FROM borrow where email=:email and isbn=:isbn;", value)

    def getBorrow(self, value):
        return self.executeRawSql("""SELECT * FROM borrow WHERE email=:email and isbn=:isbn;""", value).mappings().all()[0]

    def getAllBooks(self):
        return self.executeRawSql("SELECT * FROM book;").mappings().all()

    def getAllUsers(self):
        return self.executeRawSql("SELECT * FROM account;").mappings().all()

    def getBookAndBorrows(self):
        return self.executeRawSql("SELECT book.isbn, email, title, author FROM book LEFT JOIN borrow ON book.isbn = borrow.isbn;").mappings().all()

    def getUserByEmail(self, email):
        return self.executeRawSql("""SELECT * FROM account WHERE email=:email;""", {"email": email}).mappings().all()[0]

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
            """CREATE TABLE IF NOT EXISTS borrow (
                email TEXT REFERENCES account ON DELETE CASCADE,
                isbn TEXT REFERENCES book ON DELETE CASCADE,
                PRIMARY KEY (isbn, email)
            );
            """)
