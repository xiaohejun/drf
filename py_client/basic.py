import requests

endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint, json = {"title": 'fsdfds', 'price': 'fdsf'})
print("text:", get_response.json())
print("status_code", get_response.status_code)