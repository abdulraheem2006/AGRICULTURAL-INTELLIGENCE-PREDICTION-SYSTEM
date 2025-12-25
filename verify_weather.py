import requests
import json

try:
    print("Testing Weather Endpoint...")
    # Mocking lat/lon for Chandigarh
    response = requests.get("http://localhost:5000/api/weather?lat=30.7333&lon=76.7794")
    print(f"Status Code: {response.status_code}")
    data = response.json()
    # Check if we got real data or mock data (if api key failed, it falls back to mock)
    # The mock data has "location": "Offline Mode" or "condition" contains "Mock"
    location = data.get('current', {}).get('location', '')
    condition = data.get('current', {}).get('condition', '')
    print(f"Location: {location}")
    print(f"Condition: {condition}")
    
    if location == "Offline Mode" or "(Mock)" in condition:
        print("❌ Using Mock Data (API Key likely failed or quota exceeded)")
    else:
        print("✅ Using Real Data!")
except Exception as e:
    print(f"Error: {e}")
