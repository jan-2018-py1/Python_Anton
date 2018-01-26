from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def changeit():
    r = request.form['red']
    g = request.form['green']
    b = request.form['blue']
    color="rgb(" + r +"," + g + "," + b + ")"
    return render_template('index.html', x=color)

app.run(debug=True)