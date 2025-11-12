import imdb
import sys
from notion import create_page
from utils import convert_bytes_to_dict, pretty_print_dict, pretty_print_json
from imdb_to_notion_adaptor import convert_imdb_to_notion

def add_show_to_notion():
    """
    Takes name of the show from the user and adds it to Notion database
    """
    print("Hi! \nThis is IMDB to Notion script!\n")
    show_id = ""
    if len(sys.argv) > 1 and sys.argv[1].lower() == "--id":
        show_id = sys.argv[2]

    if show_id == "":
        search_str = input("Enter Movie or Series name: ")

        imdb_res = imdb.search_movie(search_str)

        fetched_shows = imdb_res["result"]
        if len(fetched_shows) < 1:
            print("No result!")
            # TODO: retry!
            exit()

        print("Now select one of the following:")
        pretty_print_dict(fetched_shows)

        selected_index = input("Movie index: ") 
        selected_index = int(selected_index) - 1

        show_id = fetched_shows[selected_index]["imdbID"]

    downloaded_resp = input("Is Downloaded? (N/y): ")
    is_downloaded = downloaded_resp.lower() == "y"

    imdb_data = imdb.get_movie_by_id(show_id)
    pretty_print_dict(imdb_data)

    notion_data = convert_imdb_to_notion(imdb_data["result"], is_downloaded, show_id)

    notion_res = create_page(notion_data)
    if notion_res.status_code == 200:
        print("Page added successfully!")
        pretty_print_json(notion_res.content)
    else:
        error_data = convert_bytes_to_dict(notion_res.content)
        print(error_data["message"])
