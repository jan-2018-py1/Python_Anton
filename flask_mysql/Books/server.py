from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
mysql = MySQLConnector(app, 'users')

@app.route('/')
def index():
    dbusers = mysql.query_db("SELECT * FROM books")
    return render_template("index.html", books=dbusers)

@app.route('/add')
def new_user():
    return render_template("add.html")

@app.route('/add', methods=['POST'])
def create_user():
    query = "INSERT INTO books (title, author, created) values(:1, :2, now());"
    data = {
            '1': request.form['title'],
            '2': request.form['author']
    }
    dbemail = mysql.query_db(query, data)
    return redirect('/')

@app.route('/update/<id>', methods=['POST'])
def update_user(id):
    query = "UPDATE books SET title=:1, author=:2 WHERE id=:id"
    data = {
            '1': request.form['title'],
            '2': request.form['author'],
            'id': int(id)
    }
    dbemail = mysql.query_db(query, data)
    return redirect("/")

@app.route('/edit/<id>')
def edit(id):
    return render_template("edit.html", id=id)

@app.route('/destroy/<id>')
def delete(id):
    dbemail = mysql.query_db("select title from books where id = :id", {'id':id})
    return render_template("destroy.html", book=dbemail[0]['title'])


@app.route('/delete/<title>')
def deelete(title):
    db = mysql.query_db("DELETE FROM books WHERE title=:title", {'title':title})
    return redirect("/")

app.run(debug=True)