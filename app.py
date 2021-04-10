'''
Source:

Author: Raja CSP


'''
from flask import Flask,render_template, jsonify
import random
import json
import business

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


    result_dict = business.get_data()

    return jsonify(result_dict)


if __name__ == "__main__":
    app.run( debug = True,host="0.0.0.0",port = PORT)
    