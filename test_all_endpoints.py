import requests
import json

print("=== TESTING ALL ENDPOINTS WITH REAL DATA ===\n")

# Test 1: Yield Prediction
print("1. YIELD PREDICTION TEST")
print("-" * 50)
yield_data = {
    "crop": "Wheat",
    "area": 10,
    "region": "Punjab",
    "soilType": "Loam"
}
try:
    response = requests.post("http://localhost:5000/api/predict/yield", json=yield_data)
    print(f"Status: {response.status_code}")
    result = response.json()
    print(f"Response: {json.dumps(result, indent=2)}")
except Exception as e:
    print(f"Error: {e}")

# Test 2: Soil Analysis
print("\n\n2. SOIL ANALYSIS TEST")
print("-" * 50)
soil_data = {
    "ph": 7.0,
    "n": 50,
    "p": 30,
    "k": 20
}
try:
    response = requests.post("http://localhost:5000/api/soil/analyze", json=soil_data)
    print(f"Status: {response.status_code}")
    result = response.json()
    print(f"Response: {json.dumps(result, indent=2)}")
except Exception as e:
    print(f"Error: {e}")

# Test 3: Optimization
print("\n\n3. OPTIMIZATION TEST")
print("-" * 50)
opt_data = {
    "total_area": 10,
    "water_available": 5000,
    "crops": ["Wheat", "Rice"]
}
try:
    response = requests.post("http://localhost:5000/api/optimize", json=opt_data)
    print(f"Status: {response.status_code}")
    result = response.json()
    print(f"Response: {json.dumps(result, indent=2)}")
except Exception as e:
    print(f"Error: {e}")
