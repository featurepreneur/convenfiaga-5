'''
Source:

Author: Raja CSP


'''
from flask import Flask,render_template, jsonify, request
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
'''
http://0.0.0.0:3091/api/add
http://0.0.0.0:3091/api/add?year=2017&ontario_tourist=20345&quebec_tourist=200
'''
@app.route("/api/add", methods=["GET"])
def api_add_data():

    year            = request.values.get('year')
    ontario_tourist = request.values.get('ontario_tourist')
    quebec_tourist  = request.values.get('quebec_tourist')

    result = {
        'year'    : year,
        'ontario' : ontario_tourist,
        'quebec'  : quebec_tourist

    }
    result_data = business.add_row(year, ontario_tourist, quebec_tourist)

    return jsonify(result)
   


if __name__ == "__main__":
    app.run( debug = True,host="0.0.0.0",port = PORT)
    