from flask import Flask, render_template,session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    session['counter'] += 1
    return render_template('index.html')

@app.route('/', methods=["Post"])
def twoTimes():
    session['counter'] += 2
    return render_template('index.html')

@app.route('/reset', methods=["post"])
def reset():
    session['counter'] = 0
    return render_template('index.html')

app.run(debug=True)