import requests

endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint, params={"abc": 123}, json = {"query": "hello world"})
print("text:", get_response.json())
print("status_code", get_response.status_code)