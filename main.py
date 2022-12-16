import time
import requests
from flask import Flask, render_template
from .helper import *

app = Flask(__name__)

api_root = "https://images-api.nasa.gov"

@app.route('/')
def home():
    
    collection = search_collection()
    context = build_context(collection)
    return render_template('index.html', context=context)