from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja')
def ninja():
    return render_template("ninja.html", image="img/tmnt.png")

@app.route('/ninja/<color>')
def color(color):

    if color=="blue":
        img = "img/leonardo.jpg"
    elif color=="orange":
        img = "img/michelangelo.jpg"
    elif color=="red":
        img = "img/raphael.jpg"
    elif color=="purple":
        img = "img/donatello.jpg"
    else: img = "img/notapril.jpg"
    return render_template("ninja.html", image=img)


app.run(debug=True)