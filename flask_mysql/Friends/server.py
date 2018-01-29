from flask import Flask, render_template, request, redirect
from mysqlconnection import MySQLConnector
app = Flask(__name__)

mysql = MySQLConnector(app, 'mydb')
# an example of running a query
print (mysql.query_db("SELECT * FROM friends"))

@app.route('/')
def index():
  friends = mysql.query_db("SELECT * FROM friends")
  return render_template("index.html", all_friends = friends )

@app.route('/add_friend', methods=['POST'])
def create_user():

   query = "INSERT INTO friends (name, age) values(:name, :age);"
   data = {
             'name': request.form['user_name'],
             'age':  request.form['age']
          }
   mysql.query_db(query, data)
   return redirect('/')

app.run(debug=True) # run our server