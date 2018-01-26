from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'   

@app.route('/')
def index():
  return render_template('index.html') 

@app.route('/result', methods=['POST'])
def result():
  if len(request.form['use_name']) < 1:
    flash("Name cannot be empty!")
    return redirect('/')
  if len(request.form['comments']) < 1 :
    flash("Comments cannot be empty!")
    return redirect('/')
  if len(request.form['comments']) > 120 :
    flash("Comments cannot be more than 120 characters!")
    return redirect('/')
  return render_template('result.html', name=request.form['use_name'], location=request.form['location'], lang=request.form['lang'], comment=request.form['comments']) 

app.run(debug=True)