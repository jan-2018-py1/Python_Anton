from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
mysql = MySQLConnector(app, 'users')

@app.route('/')
def index():
    dbusers = mysql.query_db("SELECT CONCAT(firstname, ' ', lastname) as name, email, created, id FROM users")
    return render_template("index.html", users=dbusers)

@app.route('/users/<id>')
def users(id):
    dbresult = mysql.query_db("SELECT CONCAT(firstname, ' ', lastname) as name, email, created, id FROM users WHERE id=:id", {'id':int(id)})
    return render_template("users.html", result = dbresult)

@app.route('/new')
def new_user():
    return render_template("new.html")

@app.route('/edit/<id>')
def edit(id):
    return render_template("edit.html", id=id)

@app.route('/delete/<id>')
def delete(id):
    db = mysql.query_db("DELETE FROM `users`.`users` WHERE id=:id", {'id':int(id)})
    return redirect("/")

@app.route('/new', methods=['POST'])
def create_user():
    query = "INSERT INTO users (firstname, lastname, email, created) values(:fname, :lname, :email, now());"
    data = {
            'fname': request.form['f_name'],
            'lname': request.form['l_name'],
            'email': request.form['email']
    }
    dbemail = mysql.query_db(query, data)
    return redirect('/new')

@app.route('/update/<id>', methods=['POST'])
def update_user(id):
    query = "UPDATE users SET firstname=:fname, lastname=:lname, email=:email WHERE id=:id"
    data = {
            'fname': request.form['f_name'],
            'lname': request.form['l_name'],
            'email': request.form['email'],
            'id': int(id)
    }
    dbemail = mysql.query_db(query, data)
    routeto ="/users/"+id
    return redirect(routeto)

app.run(debug=True)