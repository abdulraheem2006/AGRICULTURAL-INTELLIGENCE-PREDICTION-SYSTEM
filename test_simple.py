import requests

print("Testing database connection endpoint...")
try:
    response = requests.get("http://localhost:5000/api/test")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")

print("\n\nTesting yield prediction...")
try:
    response = requests.post("http://localhost:5000/api/predict/yield", json={"crop": "Wheat", "area": 10, "region": ""})
    print(f"Status: {response.status_code}")
    result = response.json()
    print(f"Response: {result}")
    if 'error' in result:
        print(f"\nERROR DETAILS: {result.get('traceback', 'No traceback')}")
except Exception as e:
    print(f"Error: {e}")
