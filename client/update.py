import requests

endpoint = "http://127.0.0.1:8000/api/1/update/"

data = {
    "tittle": "The first Book",
    "author": "Beduizenhouts"
}

web_response = requests.put(endpoint, json=data)

print(web_response.json())