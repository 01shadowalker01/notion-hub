from article import add_article_to_notion
from show import add_show_to_notion
import sys

if len(sys.argv) > 1 and sys.argv[1].lower() == "-a":
    add_article_to_notion()
else:
    add_show_to_notion()
