import requests
import json

url = 'https://jsonplaceholder.typicode.com/posts'

payload = {
    'title': 'Python Apis',
    'body': 'Aprendendo a usar APIs con Python',
    'userId': 1
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.json())
