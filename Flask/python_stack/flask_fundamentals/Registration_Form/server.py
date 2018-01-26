from flask import Flask, render_template, redirect, request, flash
import re
app=Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def submitReg():

    #First and Last Name cannot contain any numbers
    if len(request.form['first_name']) < 1 or len(request.form['last_name'])<1:
        flash("First Name and Last Name cannot be blank!")
        return redirect('/')
    elif any(i.isdigit() for i in str(request.form['first_name'])) or any(i.isdigit() for i in str(request.form['last_name'])):
        flash("First and Last Name cannot contain any numbers")
        return redirect('/')

    #Password should be more than 8 characters
    if len(request.form['pass']) < 8 :
        flash("Password should be more than 8 characters")
        return redirect('/')

    #Email should be a valid email
    if len(request.form['email'])<1:
       flash("Email cannot be blank!")
       return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email should be a valid email")
        return redirect('/')

    #Password and Password Confirmation should match
    if request.form['pass'] != request.form['conf_pass']:
        flash("The password and password Confirmation should match")
        return redirect('/')
    
    if not any(i.isdigit() for i in str(request.form['pass'])):
        flash("The password should contain contain at least one number")
        return redirect('/')
    elif str(request.form['pass']).islower():
        flash("The password should contain contain  at least one uppercase letter")
        return redirect('/')

    return render_template("success.html")


app.run(debug=True)