# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import os
from flask import Flask
from flask import render_template
from dotenv import load_dotenv


# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
def index():
    # [ # ], ] means a list inside a list?
    data = [ ['Resistor','1K','850','300','535','GRM188R60J226MEA0J','22 µF ±20% 6.3V Ceramic Capacitor X5R 0603 (1608 Metric)','bin 1'], 
             ['Resistor','1K','850','300','535','GRM188R60J226MEA0J','22 µF ±20% 6.3V Ceramic Capacitor X5R 0603 (1608 Metric)','bin 1'],
             ['Resistor','1K','850','300','535','GRM188R60J226MEA0J','22 µF ±20% 6.3V Ceramic Capacitor X5R 0603 (1608 Metric)','bin 1'],
             ['Resistor','1K','850','300','535','GRM188R60J226MEA0J','22 µF ±20% 6.3V Ceramic Capacitor X5R 0603 (1608 Metric)','bin 1'],
             ['Resistor','1K','850','300','535','GRM188R60J226MEA0J','22 µF ±20% 6.3V Ceramic Capacitor X5R 0603 (1608 Metric)','bin 1'], ]
    return render_template("index.html", data=data)


@app.route('/test')
def test():
    return 'this is a sanity check'

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    debug = os.getenv('FLASK_DEBUG')
    app.run(debug=debug)