from flask import Flask, render_template, request, redirect  
app = Flask(__name__)   

@app.route('/')
def index():
  return render_template('index.html') 

@app.route('/process', methods=['POST'])
def process():
   form_name = request.form['name']
   return render_template('process.html', name = form_name)


app.run(debug=True)