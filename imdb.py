import requests
import os
from dotenv import load_dotenv

load_dotenv()

COLLECT_API_TOKEN = os.environ["COLLECT_API_TOKEN"]

headers = {
    "authorization": COLLECT_API_TOKEN,
    "content-type": "application/json",
}

COLLECT_API_URL = "https://api.collectapi.com/imdb"

def get_movie_by_id(movie_id):
    url = f"{COLLECT_API_URL}/imdbSearchById?movieId={movie_id}"
    res = requests.get(url, headers=headers)
    return res.json()

def search_movie(movie_name):
    url = f"{COLLECT_API_URL}/imdbSearchByName?query={movie_name}"
    res = requests.get(url, headers=headers)
    return res.json()
