from flask import Flask, render_template  
app = Flask(__name__)                     
                                          
@app.route('/')                           
def index():
  return render_template('index.html')    

@app.route('/ninjas')
def ninjas():
  return render_template('ninjas.html')    

@app.route('/dojos/new')
def news():
  return render_template('dojos.html', button_name="Submit")    
 

app.run(debug=True)    