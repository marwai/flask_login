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
            # During second attempt, the penultimate attempt will flash a message stating "one attempt remaining" 
            if int(attempt) == 2:
                flash("One attempt remaining")
            # If the third and final attempt is a failure, then the page is sent to an error page 
            if attempt == 3:
                abort(404)
            # After every attempt the counter is increased by 1 
            else:
                attempt += 1
                session['attempt'] = attempt
                # error message is printed 
                error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were just logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)
```