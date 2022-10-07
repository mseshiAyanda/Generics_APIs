import requests

article_id = input('which article do you want to delete?')

try:
    article_id = int(article_id)
except:
    article_id = None
    print(f'{article_id} is not valid id')    

if article_id:
     endpoint = f"http://127.0.0.1:8000/api/{article_id}/delete"

     get_response = requests.delete(endpoint)
  
print(get_response.status_code, get_response.status_code==204)


