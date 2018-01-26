from flask import Flask, render_template, redirect, session, request
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    session['number'] = random.randrange(0,100)
    return render_template('index.html')

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/', methods=['POST'])
def game():
    userAnswer = request.form['answer']
    
    try:
        if int(userAnswer) < session['number']:
            
            return render_template('index.html', answer="less" )
        
        elif int(userAnswer) > session['number']:
            return render_template('index.html', answer="more")
        
        else: 
            return render_template('index.html', answer="won", cl='style=display:none', num=session['number'])
    except:
        return render_template('index.html')

@app.route('/res', methods=['POST'])
def reset():
    session['counter'] = random.randrange(0,100)
    return redirect('/')

@app.route('/get')
def printit():
    return(str(session['number']))

if __name__ =='__main__':
    app.run(debug=True)