from datetime import datetime, timezone
import os
import re
from dotenv import load_dotenv

load_dotenv()

SHOWS_DATABASE_ID = os.environ["SHOWS_DATABASE_ID"]

# Get current time in UTC
current_time = datetime.now(timezone.utc).isoformat()


def convert_imdb_to_notion(imdb_data, is_downloaded, show_id):
    """
    converts retrieved data from imdb to notion format
    """
    year_str = re.sub(r"\D", "", imdb_data["Year"])
    duration_mins_str = re.sub(r"\D", "", imdb_data["Runtime"])
    notion_data = {
        "created_time": current_time,
        "cover": {"external": {"url": imdb_data["Poster"]}},
        "parent": {"database_id": SHOWS_DATABASE_ID},
        "properties": {
            "Name": get_text_type(imdb_data["Title"]),
            "Type": {
                "multi_select": [
                    {
                        "name": "TV Series"
                        if imdb_data["Type"] == "series"
                        else "Movie",
                    }
                ]
            },
            "Cast": {"multi_select": get_multi_select(imdb_data["Actors"])},
            "Genre": {"multi_select": get_multi_select(imdb_data["Genre"])},
            "Year": {"number": to_int(year_str)},
            "Rate": {"select": {"name": imdb_data["Rated"]}},
            "URL": {"url": "https://www.imdb.com/title/" + show_id},
            "Imdb Score": {"number": to_float(imdb_data["imdbRating"])},
            "Additional information ": get_text_type(
                imdb_data["Plot"], is_rich_text=True
            ),
            "Director": get_text_type(imdb_data["Director"], is_rich_text=True),
            "Duration": get_text_type(imdb_data["Runtime"], is_rich_text=True),
            "Duration (mins)": {"number": to_int(duration_mins_str)},
            "Downloaded": {"checkbox": is_downloaded},
        },
    }

    return notion_data


def get_text_type(text, is_rich_text=False):
    """
    converts text data to notion's text or rich_text format
    """
    value = [
        {
            "type": "text",
            "text": {
                "content": text,
            },
            "annotations": {
                "bold": False,
                "italic": False,
                "strikethrough": False,
                "underline": False,
                "code": False,
                "color": "default",
            },
            "plain_text": text,
            "href": "None",
        }
    ]
    result = {"rich_text": value} if is_rich_text else {"title": value}

    return result


def get_multi_select(data_str):
    """
    converts text data to multi_select format
    """
    array = data_str.split(",")
    select_data = list(map(lambda item: {"name": item.strip()}, array))
    return select_data

def to_int(data_str):
    try:
        return int(data_str)
    except:
        return None

def to_float(data_str):
    try:
        return float(data_str)
    except:
        return None
