import requests
import json
response_API = requests.get(
    'https://gmail.googleapis.com/$discovery/rest?version=v1')
# print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data)
info = parse_json['description']
print("Info about API:\n", info)
key = parse_json['parameters']['key']['description']
print("\nDescription about the key:\n", key)
