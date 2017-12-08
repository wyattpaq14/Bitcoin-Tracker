import requests
from flask import render_template, request, flash, Flask
import json
from threading import Timer
import time

app = Flask(__name__)

myList = ""
 
@app.route("/")
def index():

    url = 'http://api.coindesk.com/v1/bpi/currentprice.json'

    r = requests.get(url)
 
    json_data = r.text
    python_obj = json.loads(json_data)
    
    myList = python_obj["bpi"]["USD"]["rate_float"]

    return render_template('index.html', variable=myList)



 
if __name__ == "__main__":
    app.run()