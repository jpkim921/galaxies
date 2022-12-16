import random
import requests
import urllib.parse
from datetime import date


def search_collection(pageNum=0, search_term="galaxy"):
    search_url = "https://images-api.nasa.gov/search"
    today = date.today()

    params = {
        'q': urllib.parse.quote(search_term),
        'year_start': str(today.year - 5),
        'page': str(pageNum if pageNum else 1)
    }

    response = requests.get(search_url, params=params)
    collection = response.json()['collection']
    return collection

def get_item_count(collection):
    return collection['metadata']['total_hits']

def get_rand_page(collection):
    total_items = get_item_count(collection)
    if total_items % 100 > 0:
        total_pages = (total_items // 100) + 1
        return random.randint(1, total_pages)
    else:
        total_items // 100

def get_rand_item(collection):
    total_items = len(collection['items'])
    return random.randint(0, total_items)

def get_item(pageNum: int, itemNum: int):
    col = search_collection(pageNum=pageNum)
    return col['items'][itemNum]

    

search_input = 'galaxy'
col = search_collection()
pageNum = get_rand_page(col)
itemNum = get_rand_item(col)
print(get_item(pageNum, itemNum))



