import random
import requests
import urllib.parse
from datetime import date


def search_collection(pageNum=0, search_term="galaxy"):
    search_url = "https://images-api.nasa.gov/search"
    today = date.today()

    params = {
        'media_type': 'image',
        'q': urllib.parse.quote(search_term),
        'year_start': str(today.year - 5),
        'page': str(pageNum if pageNum else 1)
    }

    response = requests.get(search_url, params=params)
    collection = response.json()['collection']
    return collection

def get_item_count(collection):
    return collection['metadata']['total_hits']

def get_rand_pageNum(collection):
    total_items = get_item_count(collection)
    return total_items // 100
    # uses the original collection, so index will be out of range
    # if total_items % 100 > 0:
    #     total_pages = (total_items // 100) + 1
    #     return random.randint(1, total_pages)
    # else:
    #     return total_items // 100

def get_rand_itemNum(collection):
    total_items = len(collection['items'])
    return random.randint(0, total_items)

def get_item(collection):
    pageNum = get_rand_pageNum(collection)
    itemNum = get_rand_itemNum(collection)
    print(pageNum, itemNum)
    col = search_collection(pageNum=pageNum)
    return col['items'][itemNum]

def get_image_hrefs(item):
    hrefs = requests.get(item['href'])
    return hrefs.json()
import pprint

def build_context(collection):
    item = get_item(collection)
    context = {
        'images': get_image_hrefs(item),
        'title': item['data'][0]['title'],
        'photographer': item['data'][0].get('photographer', "n/a"),
        'description': item['data'][0]['description']
    }
    return context
