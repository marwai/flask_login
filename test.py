# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session, flash, abort
from functools import wraps
# create the application object
app = Flask(__name__)
# config
app.secret_key = 'myuniquekey'
# login required decorator

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


@app.route('/', methods=['GET'])
@login_required
def home():
    session['attempt'] = 1
    return render_template('index.html')  # render a template
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template
# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            attempt = int(session.get('attempt'))
            if attempt == 2:
                flash("This is your last chance")
                # attempt += 1
                # session['attempt'] = attempt
            if attempt == 3:
                flash('You have been logged out.')
                abort(404)
            else:
                attempt += 1
                session['attempt'] = attempt
                error = 'Invalid Credentials. Please try again'
        else:
            # Giving link to user page if username/password correct
            return "<h3> Access your user page <a href=www.google.com> here </a> </h3>"
            # session['logged_in'] = True
            # flash('You were logged in.')
            # return redirect(url_for('home'))
    return render_template('login.html', error=error)
@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('welcome'))

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True) #this ensures to update any changes without re-running the app.
#error/exception - look at the line number
#Check errors and exceptions in the browser