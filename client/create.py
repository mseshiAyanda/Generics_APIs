import requests

endpoint = "http://127.0.0.1:8000/api/create/"

data = {
    "tittle": "again",
    "author": "Sbusiso"
}

web_response = requests.post(endpoint, json=data)
print(web_response.json())