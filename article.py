import os
from datetime import datetime, timezone
from dotenv import load_dotenv
import notion
from utils import convert_bytes_to_dict, pretty_print_json

load_dotenv()

ARTICLES_DATABASE_ID = os.environ["ARTICLES_DATABASE_ID"]

def create_article_data(title, url, is_finished):
    """
    This function handles the organization and formatting of article data
    to be compatible with Notion's page structure.

    Args:
        title (str): The title of the article to be created.
        url (str): The URL of the article to be created.
        is_finished (bool): Indicates if the article's reading has been finished.

    Returns:
        Dict: The structured article data ready for Notion integration.
    """
    current_time = datetime.now(timezone.utc).isoformat()
    article_data = {
        "created_time": current_time,
        "parent": {"database_id": ARTICLES_DATABASE_ID},
        "properties": {
            "Name": {
                "title": [
                    {
                        "type": "text",
                        "text": {
                            "content": title,
                        },
                        "annotations": {
                            "bold": False,
                            "italic": False,
                            "strikethrough": False,
                            "underline": False,
                            "code": False,
                            "color": "default",
                        },
                        "plain_text": title,
                        "href": "None",
                    }
                ]
            },
            "Link": {
                "url": url
            },
            "Status": {
                "status": {
                    "name": "Reading Finished" if is_finished else "Not started"
                }
            }
        }
    }
    return article_data


def add_article_to_notion():
    """
    Takes url of the article from the user and adds it to Notion database
    """
    print("Hi! \nThis is Article to Notion script!\n")
    article_title = input("Enter Article Title: ")
    article_url = input("Enter Article URL: ")

    finished_resp = input("Is Finished? (N/y): ")
    is_finished = finished_resp.lower() == "y"

    article_data = create_article_data(article_title, article_url, is_finished)

    notion_res = notion.create_page(article_data)
    if notion_res.status_code == 200:
        print("Page added successfully!")
        pretty_print_json(notion_res.content)
    else:
        error_data = convert_bytes_to_dict(notion_res.content)
        print(error_data["message"])