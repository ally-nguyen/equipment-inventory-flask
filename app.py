# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import os
from flask import Flask
from flask import render_template
from dotenv import load_dotenv
from flask import Flask, request, jsonify


# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
#d ef submit is used to process/handle the submitted data 
def submit():
    data = request.json
    component = data.get("component")
    size = data.get("size")

    # saves data, stores it (processes data) is database using JSON 
    response_data = {
        # key-value
        "component":component,
        "size":size
    }
    # return a JSON response to client with code 200 (means request was successful)
    return jsonify(response_data),200

@app.route('/test')
def test():
    return 'this is a sanity check'

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    debug = os.getenv('FLASK_DEBUG')
    app.run(debug=debug)