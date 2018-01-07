import requests
from flask import render_template, request, flash, Flask
import json
from threading import Timer
import time

app = Flask(__name__)

myList = ""
 
@app.route("/")
def index():


    return render_template('index.html', variable=myList)



 
if __name__ == "__main__":
    app.run()