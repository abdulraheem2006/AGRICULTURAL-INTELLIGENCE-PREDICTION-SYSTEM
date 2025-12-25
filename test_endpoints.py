import requests
import json

# Test Soil Analysis
print("=" * 50)
print("Testing Soil Analysis Endpoint")
print("=" * 50)

soil_data = {
    "ph": 7.0,
    "n": 50,
    "p": 30,
    "k": 20
}

try:
    response = requests.post("http://localhost:5000/api/soil/analyze", json=soil_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response:\n{json.dumps(response.json(), indent=2)}")
except Exception as e:
    print(f"Error: {e}")

print("\n" + "=" * 50)
print("Testing Optimization Endpoint")
print("=" * 50)

optimize_data = {
    "total_area": 10,
    "water_available": 5000,
    "crops": ["Wheat", "Rice", "Maize", "Sugarcane"]
}

try:
    response = requests.post("http://localhost:5000/api/optimize", json=optimize_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response:\n{json.dumps(response.json(), indent=2)}")
except Exception as e:
    print(f"Error: {e}")
