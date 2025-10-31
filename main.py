from show import add_show_to_notion
import sys

print(sys.argv)
if len(sys.argv) > 1 and sys.argv[1].lower() == "-a":
    # add article to notion
    print("add article to notion...")
else:
    add_show_to_notion()
