import json

def pretty_print_json(arg):
    parsed = json.loads(arg)
    formatted_str = json.dumps(parsed, indent=2)
    print(formatted_str)

def pretty_print_dict(arg):
    formatted_str = json.dumps(arg, indent=2)
    print(formatted_str)

def convert_bytes_to_dict(bytes_data):
    json_string = bytes_data.decode('utf-8')
    dictionary = json.loads(json_string)
    return dictionary