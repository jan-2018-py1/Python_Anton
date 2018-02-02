from flask import Flask, render_template, redirect, request, flash
from mysqlconnection import MySQLConnector
import re
import md5

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app, 'mydb')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lgn')
def loginpage():
    return render_template('login.html')

@app.route('/', methods=['POST'])
def createuser():
    query = "SELECT email FROM login_data where email =:email"
    data = {
            'email': request.form['email']
    }
    dbemail = mysql.query_db(query, data)
    
    try:
        if request.form['email'] == dbemail[0]['email']:
            flash("The entered email exists in the DB!")
            return redirect('/')
    except IndexError:
        pass

    if not EMAIL_REGEX.match(request.form['email']):
        flash("Email should have a valid format")
        return redirect('/')
    if len(request.form['f_name']) < 2:
        flash("The first name should be more than 2 characters")
        return redirect('/')
    elif len(request.form['l_name']) < 2:
        flash("The last name should be more than 2 characters")
        return redirect('/')
    if len(request.form['pass']) <= 8:
        flash("The password should be more than 8 characters")
        return redirect('/')
    elif request.form['pass'] != request.form['c_pass']:
        flash("The password and confirm password should match")
        return redirect('/')
    else:
        hashedpass = md5.new(request.form['pass']).hexdigest()
        query = "INSERT INTO login_data (f_name, l_name, email, password, created) values(:fname, :lname, :email, :pass , now());"
        data = {
            'fname': request.form['f_name'],
            'lname': request.form['l_name'],
            'email': request.form['email'],
            'pass':  hashedpass
        }
        dbemail = mysql.query_db(query, data)
    return redirect('/lgn')



@app.route('/lgn',  methods=['POST'])
def login():
    
    if len(request.form['pass']) < 1:
        flash("Password cannot be blank!")
        return redirect('/lgn')
    elif len(request.form['email']) < 1: 
        flash("Email cannot be blank!")
        return redirect('/lgn')
    
    hashed_password = md5.new(request.form['pass']).hexdigest()

    query = "SELECT f_name,l_name FROM login_data where email =:email and password =:pass"
    data = {
            'email': request.form['email'],
            'pass': hashed_password 
    }
    login_pass = mysql.query_db(query, data)
    
    if len(login_pass)<1:
        flash("login failed: email and/or password invalid")      
        return redirect('/lgn')
    else:
        message = " " + str(login_pass[0]['f_name']) +" "+ str(login_pass[0]['l_name'])
        return render_template('/success.html', username = message)

app.run(debug=True)