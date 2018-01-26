from flask import Flask, render_template, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

def getDate():
    return  str(datetime.now())

log = 'the game is started! ' + getDate()+'\n'

@app.route('/')
def index():
    if 'number' not in session:
        session['number']=0 
    if 'log' not in session:
        session['log']=[log] 
    return render_template('index.html', gold=session['number'])

@app.route('/process_money/<loc>', methods=['POST'])
def process_money(loc):
    if loc == "Farm":
        money = makeGold(10, 21)
        message = "Earned " + str(money)+ " gold from the farm! " + getDate()+'\n'
        session['number']+=money
        session['log'].append(message)
    elif loc == "Cave":
        money = makeGold(5, 11)
        message = "Earned " + str(money)+ " gold from the cave! " + getDate()+'\n'
        session['number']+=money
        session['log'].append(message)
    elif loc == "House":
        money = makeGold(2, 6)
        message = "Earned " + str(money)+ " gold from the house! " + getDate()+'\n'
        session['number']+=money
        session['log'].append(message)
    else:
        if casion=="win":
            money = makeGold(0, 51)
            message = "Earned " + str(money)+ " gold from the casino! " + getDate()+'\n'
            session['number']+=money
            session['log'].append(message)
        else: 
            money = makeGold(0, 51)
            message = "Entered a casino and lost " + str(money) + " gold... Ouch " + getDate()+'\n'
            session['number']-=money
            session['log'].append(message)
    return  redirect('/')


@app.route('/reset')
def reset():
    session['number'] = 0
    session['log'] = []
    return redirect('/')


def casion():
    result = random.randrange(0,100)
    if result<30:
        return "win"
    else: return "lost"

def makeGold(min, max):
    result = random.randrange(min,max)
    return result


app.run(debug=True)