import requests
import os
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.environ["NOTION_TOKEN"]

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2025-09-03",
}

def create_page(data: dict):
    create_url = "https://api.notion.com/v1/pages"

    res = requests.post(create_url, headers=headers, json=data)
    return res
