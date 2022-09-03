from flask import request, session, redirect, url_for, render_template, flash

from . models import Models
from . forms import AddBorrowerForm, SignUpForm, SignInForm

from src import app

models = Models()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/books')
def show_books():
    if session['user_available']:
        booksAndBorrows = models.getBookAndBorrows()
        return render_template('books.html', booksAndBorrows=booksAndBorrows)
    flash('User is not Authenticated')
    return redirect(url_for('index'))


@app.route('/add', methods=['GET', 'POST'])
def add_borrower():
    if session['user_available']:
        borrower = AddBorrowerForm(request.form)
        us = models.getUserByEmail(session['current_user'])
        if request.method == 'POST':
            models.addBorrower({"email": borrower.email.data, "isbn": borrower.isbn.data})
            return redirect(url_for('show_books'))
        return render_template('add.html', borrower=borrower)
    flash('User is not Authenticated')
    return redirect(url_for('index'))


@app.route('/delete/<email>/<isbn>', methods=('GET', 'POST'))
def delete_book(isbn, email):
    models.deleteBorrow({"email": email, "isbn": isbn})
    return redirect(url_for('show_books'))


@app.route('/update/<email>/<isbn>', methods=('GET', 'POST'))
def update_book(isbn, email):
    br = models.getBorrow({"email": email, "isbn": isbn})
    borrower = AddBorrowerForm(request.form, obj=br)
    if request.method == 'POST':
        models.updateBorrower({"email": borrower.email.data, "isbn": borrower.isbn.data})
        return redirect(url_for('show_books'))
    return render_template('update.html', borrower=borrower)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    signupform = SignUpForm(request.form)
    if request.method == 'POST':
        models.addUser({"email": signupform.email.data, "password": signupform.password.data})
        return redirect(url_for('signin'))
    return render_template('signup.html', signupform=signupform)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    signinform = SignInForm(request.form)
    if request.method == 'POST':
        em = signinform.email.data
        log = models.getUserByEmail(em)
        if log.password == signinform.password.data:
            session['current_user'] = em
            session['user_available'] = True
            return redirect(url_for('show_books'))
    return render_template('signin.html', signinform=signinform)


@app.route('/about_user')
def about_user():
    if session['user_available']:
        user = models.getUserByEmail(session['current_user'])
        return render_template('about_user.html', user=user)
    flash('You are not a Authenticated User')
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.clear()
    session['user_available'] = False
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
