from flask import request, session, redirect, url_for, render_template, flash

from . models import Models
from . forms import AddReaderForm, SignUpForm, SignInForm

from src import app

models = Models()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/books')
def show_books():
    try:
        if session['user_available']:
            booksAndAssignments = models.getBooksAndAssignments()
            return render_template('books.html', booksAndAssignments=booksAndAssignments)
        flash('User is not Authenticated')
        return redirect(url_for('index'))
    except Exception as e:
        flash(str(e))


@app.route('/add', methods=['GET', 'POST'])
def add_reader():
    try:
        if session['user_available']:
            reader = AddReaderForm(request.form)
            if request.method == 'POST':
                models.addAssignment({"email": reader.email.data, "isbn": reader.isbn.data})
                return redirect(url_for('show_books'))
            return render_template('add.html', reader=reader)
    except Exception as e:
        flash(str(e))
    flash('User is not Authenticated')
    return redirect(url_for('index'))


@app.route('/delete/<email>/<isbn>', methods=('GET', 'POST'))
def delete_book(isbn, email):
    try:
        models.deleteAssignment({"email": email, "isbn": isbn})
        return redirect(url_for('show_books'))
    except Exception as e:
        flash(str(e))
        return redirect(url_for('index'))


@app.route('/update/<email>/<isbn>', methods=('GET', 'POST'))
def update_book(isbn, email):
    try:
        br = models.getAssignment({"email": email, "isbn": isbn})
        reader = AddReaderForm(request.form, obj=br)
        if request.method == 'POST':
            models.updateAssignment({"email": reader.email.data, "isbn": reader.isbn.data})
            return redirect(url_for('show_books'))
        return render_template('update.html', reader=reader)
    except Exception as e:
        flash(str(e))
        return redirect(url_for('index'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    try:
        signupform = SignUpForm(request.form)
        if request.method == 'POST':
            models.addProfessor({"email": signupform.email.data, "password": signupform.password.data})
            return redirect(url_for('signin'))
        return render_template('signup.html', signupform=signupform)
    except Exception as e:
        flash(str(e))
        return redirect(url_for('index'))


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    try:
        signinform = SignInForm(request.form)
        if request.method == 'POST':
            em = signinform.email.data
            log = models.getProfessorByEmail(em)
            if log.password == signinform.password.data:
                session['current_user'] = em
                session['user_available'] = True
                return redirect(url_for('show_books'))
            else:
                flash('Cannot sign in')
        return render_template('signin.html', signinform=signinform)
    except Exception as e:
        flash(str(e))
        return redirect(url_for('index'))


@app.route('/about_user')
def about_user():
    try:
        if session['user_available']:
            user = models.getProfessorByEmail(session['current_user'])
            return render_template('about_user.html', user=user)
        flash('You are not a Authenticated User')
        return redirect(url_for('index'))
    except Exception as e:
        flash(str(e))
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    try:
        session.clear()
        session['user_available'] = False
        return redirect(url_for('index'))
    except Exception as e:
        flash(str(e))
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
