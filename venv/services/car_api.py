import os
import requests

from dotenv import load_dotenv
import requests

load_dotenv()
# Escrevendo o cliente da API de carros
class CarApi:
    
    
    def __init__(self):
        self.base_url = os.getenv("BASE_URL")
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")
        self.token = self.__get_token()
        self.__headers = {
            'Authorization': f'Bearer {self.token}',
        }
        
        
    
    def __get_token(self):
        payload = {
            'email': self.email,
            'password': self.password,
        }
        response = requests.post(
            url=f'{self.base_url}/api/v1/auth/token',
            json=payload
        )
        if response.status_code == 200:
            return response.json().get('access_token')
        else:
            raise Exception("Failed to get token")
    
    def get_cars(self):
        response = requests.get(
            url=f'{self.base_url}/api/v1/cars',
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to fetch cars")
        
    def get_car_by_id(self, car_id):
        response = requests.get(
            url=f'{self.base_url}/api/v1/cars/{car_id}',
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch car with ID {car_id}")    
        
    def create_car(self, car_data):
        response = requests.post(
            url=f'{self.base_url}/api/v1/cars',
            headers=self.__headers,
            json=car_data
        )
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception("Failed to create car")
        
    def update_car(self, car_id, car_data):
        response = requests.put(
            url=f'{self.base_url}/api/v1/cars/{car_id}',
            headers=self.__headers,
            json=car_data
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to update car with ID {car_id}")
        
    def delete_car(self, car_id):
        response = requests.delete(
            url=f'{self.base_url}/api/v1/cars/{car_id}',
            headers=self.__headers
        )
        if response.status_code == 204:
            return True
        else:
            raise Exception(f"Failed to delete car with ID {car_id}")            