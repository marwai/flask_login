# Acceptance Criteria
* User must be able to login with username and password
* be directed to homepage/index.html if unsuccessful redirected to error page 
404/customised page with message of your choice
* There should be 2 minimum buttons on the login page - Submit and Cancel
2 text boxes to take information in 
 
 

#### importing flask modules:
```bash
from flask import *
from functools import wraps
```
#### Directing to main page
```bash
@app.route("/")
def welcome ():
    return render_template('welcome.html')
```
#### Creating login function
```bash
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
                attempt += 1
                session['attempt'] = attempt
                error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were just logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)
```