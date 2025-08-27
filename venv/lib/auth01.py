"""Criando um arquivo de autenticação Python com token
"""
    
import requests

url = 'https://findworrk.dev/api/v1/jobs/'

headers = {
    'Authorization': 'Token 1234567890abcdef',
}

response = requests.get(url, headers=headers)
print(response.status_code)
print(response.json())
    