# Import the flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session, flash, abort
from functools import wraps

#Create the application object
app = Flask(__name__)

app.secret_key = "key"

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

# use decorators to link the function to a url
# called key in login page, login required object will catch it, flashes message to log in
@app.route('/', methods =['GET'])
# If user sends a Git request to index page and not logged in, meaning not key
@login_required
def home():
    session['attempt'] = 1
    return render_template("index.html")
    # return "Hello, world!"

# Similarly when the welcome
@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    #     flash("last chance")
    if request.method == 'POST':
        if request.form['username'] != 'Marwai' or request.form['password'] != 'password':
            attempt = session.get('attempt')
            if int(attempt) == 2:
                flash("One attempt remaining")
            # if attempt == 0:
            if attempt == 3:
                abort(404)
            else:
                # during each login attempt, the counter increases
                attempt += 1
                session['attempt'] = attempt
                # prints the message
                error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            # Flask provides a really simple way to give feedback to a user with the flashing system.
            flash('You were just logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('welcome'))

if __name__ == '__main__':
    app.run(debug=True)