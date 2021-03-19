import requests
import json


response = requests.get("https://api.github.com/users")


json_response = json.loads(response.content)

for user in json_response:
    user_name = user["login"]
    url = user["url"]
    print(user_name, url)
