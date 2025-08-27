# Python APIs Learning Journey

## Introduction
This repository documents my learning journey with Python APIs. It includes examples, notes, and projects that demonstrate my progress and understanding.

## Topics Covered
- **Introduction to APIs**: Understanding what APIs are and how they work.
- **HTTP Methods**: GET, POST, PUT, DELETE, and their use cases.
- **Working with Requests Library**: Sending HTTP requests and handling responses.
- **Building APIs with Flask**: Creating endpoints and handling routes.
- **Authentication**: Implementing API keys, OAuth, and JWT.
- **Error Handling**: Managing errors and exceptions in API responses.
- **Consuming External APIs**: Integrating third-party APIs into Python applications.
- **Testing APIs**: Writing unit tests for API endpoints.

## Project Structure
### `/services/car_api.py`
This file contains the `CarApi` class, which is a client for interacting with a car API. It includes methods for:
- **Authentication**: Fetching an access token using email and password.
- **Fetching Cars**: Retrieving all cars or a specific car by ID.
- **Creating Cars**: Adding a new car to the API.
- **Updating Cars**: Modifying an existing car's details.
- **Deleting Cars**: Removing a car from the API.

### `/main.py`
This file demonstrates how to use the `CarApi` class. It includes examples of:
- Fetching all cars.
- Creating a new car.
- Fetching a car by its ID.
- Updating a car's details.
- Deleting a car.

## Examples
### Example: Sending a GET Request
```python
import requests

response = requests.get('https://api.example.com/data')
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
```

### Example: Creating a Flask API
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Hello, World!")

if __name__ == '__main__':
    app.run(debug=True)
```

## Future Learning Goals
- Explore Django REST Framework.
- Learn about GraphQL APIs.
- Dive deeper into API security best practices.

## Conclusion
This repository will continue to grow as I learn more about Python APIs. Feedback and suggestions are welcome!