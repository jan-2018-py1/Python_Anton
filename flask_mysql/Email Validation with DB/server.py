from flask import Flask, render_template, request, redirect, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)

app.secret_key = 'KeepItSecretKeepItSafe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

mysql = MySQLConnector(app, 'mydb')
# an example of running a query
print (mysql.query_db("SELECT * FROM emails"))

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/success')
def success():
  return render_template("success.html", emails = mysql.query_db("SELECT * FROM emails"))

@app.route('/', methods=['POST'])
def create_email():

    if len(request.form['email'])<1:
        flash("Email cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email should be a valid email")
        return redirect('/')
    else:
        query = "INSERT INTO emails (email, date_created) values(:email, now());"
        data = {
            'email': request.form['email']
        }
        mysql.query_db(query, data)
    return redirect('/success')

@app.route('/delete_data/<value>', methods=['POST'])
def delete_email(value):
    print value
    query = "DELETE FROM emails WHERE email = :id"
    mysql.query_db(query, {'id': value})
    return redirect('/success')

app.run(debug=True)