from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector
import re
import md5

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app, 'wall')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/lgn')
def loginpage():
    return render_template('login.html')

@app.route('/', methods=['POST'])
def createuser():
    query = "SELECT email FROM users where email =:email"
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
        query = "INSERT INTO users (first_name, last_name, email, password, created_at) values(:fname, :lname, :email, :pass , now());"
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

    query = "SELECT id, first_name FROM users where email =:email and password =:pass"
    data = {
            'email': request.form['email'],
            'pass': hashed_password 
    }
    login_pass = mysql.query_db(query, data)
    
    if len(login_pass)<1:
        flash("login failed: email and/or password invalid")      
        return redirect('/lgn')
    else:
        session['user'] = str(login_pass[0]['id'])
        return redirect('/wall')

@app.route('/lgoff')
def lgoff():
    session.clear()
    return redirect('/lgn')

@app.route('/wall')
def wall():
    if 'user' not in session:
        return redirect('/lgn')
    else:
        message = mysql.query_db("SELECT users.first_name, users.last_name, message.created_at, message.id, message.message FROM message LEFT JOIN users ON message.users_id = users.id")
        comments = mysql.query_db("SELECT users.id, users.first_name, users.last_name, comments.comments, comments.created_at, comments.message_id FROM users JOIN comments ON comments.users_id = users.id")
        user_name = mysql.query_db("SELECT first_name FROM users where id =:id", {'id':int(session['user'])})
        if len(message)<1:
            return render_template('/wall.html', name=user_name[0]["first_name"])
        if len(message)>1 and len(comments)<1:
            return render_template('/wall.html', name=user_name[0]["first_name"], message=message, flag = True)
        else:
            return render_template('/wall.html', name=user_name[0]["first_name"], message=message, flag = True, comments=comments)


@app.route('/message',  methods=['POST'])
def post_message():
    if len(request.form['message'])<1:
        return redirect("/wall")
    query = "INSERT INTO message (users_id, message, created_at) VALUES (:user_id, :message, now())"
    data = {
            'user_id': int(session['user']),
            'message': request.form['message'] 
    }
    respond = mysql.query_db(query, data)
    return redirect("/wall")

@app.route('/comment/<id>',  methods=['POST'])
def post_comment(id):
    if len(request.form['comment'])<1:
        return redirect("/wall")
    query = "INSERT INTO comments (message_id, users_id, comments, created_at) VALUES (:message_id, :users_id, :text, now())"
    data = {
            'message_id': int(id),
            'users_id': int(session['user']),
            'text': request.form['comment']
    }
    respond = mysql.query_db(query, data)
    return redirect("/wall")






app.run(debug=True)