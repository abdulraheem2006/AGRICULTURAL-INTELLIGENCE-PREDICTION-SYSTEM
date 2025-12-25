import requests
import sys

try:
    response = requests.get('http://localhost:5000/api/health', timeout=2)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    if response.status_code == 200:
        print("Backend is running!")
    else:
        print("Backend returned unexpected status.")
except requests.exceptions.ConnectionError:
    print("Connection refused. Backend is likely NOT running.")
except Exception as e:
    print(f"An error occurred: {e}")
