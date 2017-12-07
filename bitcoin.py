import requests
from flask import render_template, request, flash, Flask
from bs4 import BeautifulSoup
import json
from threading import Timer

app = Flask(__name__)

myList = ""
 
@app.route("/")
def index():
    Timer(5.0, index).start()

    url = 'http://api.coindesk.com/v1/bpi/currentprice.json'

    r = requests.get(url)
 
    json_data = r.text
    python_obj = json.loads(json_data)
    
    myList = python_obj["bpi"]["USD"]["rate_float"]


    return render_template('index.html', variable=myList)
index()

 
if __name__ == "__main__":
    app.run()