import time
import requests
from flask import Flask
from .helper import *

app = Flask(__name__)

api_root = "https://images-api.nasa.gov"

@app.route('/')
def home():
    collection = search_collection()
    item = get_item(collection)
    return item