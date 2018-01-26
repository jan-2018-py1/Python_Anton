from flask import Flask, render_template, request, redirect  
app = Flask(__name__)   

@app.route('/')
def index():
  return render_template('index.html') 

@app.route('/result', methods=['POST'])
def result():
  return render_template('result.html', name=request.form['use_name'], location=request.form['location'], lang=request.form['lang'], comment=request.form['comments']) 

app.run(debug=True)