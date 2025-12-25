import requests
import json

# Test just optimization with better error handling
optimize_data = {
    "total_area": 10,
    "water_available": 5000,
    "crops": ["Wheat", "Rice", "Maize"]
}

try:
    response = requests.post("http://localhost:5000/api/optimize", json=optimize_data)
    print(f"Status Code: {response.status_code}")
    result = response.json()
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"Success:\n{json.dumps(result, indent=2)}")
except Exception as e:
    print(f"Exception: {e}")
