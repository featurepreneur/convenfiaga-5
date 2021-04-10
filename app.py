'''
Source:

Author: Raja CSP


'''
from flask import Flask,render_template, jsonify
import random
import json

app  = Flask(__name__)
PORT = 3091

    
@app.route("/", methods=["GET","POST"])
def startpy():

    result = {

        "Greetings" : "Tactlabs welcomes you"
    }

    return render_template("index.html", result = result)

'''
http://0.0.0.0:3091/api/data
'''

@app.route("/api/data", methods=["GET"])
def api_get_data():

    ontario_data = [20113, 21019, 22037, 22844, 23903]

    quebec_data = [600, 1000, 642, 897, 689]

    result_dict = {
        'ontario' : ontario_data,
        'quebec'  : quebec_data
    }

    return jsonify(result_dict)


if __name__ == "__main__":
    app.run( debug = True,host="0.0.0.0",port = PORT)
    