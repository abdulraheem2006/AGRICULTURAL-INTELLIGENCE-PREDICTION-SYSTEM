
import requests
import json
import time

def test_endpoints():
    base_url = "http://localhost:5000/api"
    
    # 1. Test Yield Prediction (RF Model)
    print("\ntesting /predict/yield (Random Forest)...")
    payload = {
        "crop": "Rice",
        "area": 5,
        "region": "Punjab", # Should match trained state labels or degrade gracefully
        "soilType": "Clay",
        "rainfall": 1200,
        "fertilizer": 150
    }
    try:
        r = requests.post(f"{base_url}/predict/yield", json=payload)
        if r.status_code == 200:
            data = r.json()
            print("✅ Success!")
            print(f"  Predicted Yield: {data['predictedYield']}")
            print(f"  Confidence: {data['confidence']}")
            print(f"  Source: {data['data_source']}")
            print(f"  Algorithm: {data['algorithm']}")
            
            if "Random Forest" not in data.get('algorithm', ''):
                print("  ⚠️ WARNING: Algorithm name indicates fallback might be active?")
        else:
            print(f"❌ Failed: {r.status_code} - {r.text}")
    except Exception as e:
        print(f"❌ Error: {e}")

    # 2. Test Optimization (MILP)
    print("\ntesting /optimize (MILP)...")
    payload = {
        "total_area": 20,
        "water_available": 10000000, # Large amount to allow flexibility
        "crops": ["Wheat", "Rice", "Maize", "Sugarcane"]
    }
    try:
        r = requests.post(f"{base_url}/optimize", json=payload)
        if r.status_code == 200:
            data = r.json()
            print("✅ Success!")
            print(f"  Total Profit: {data['totalProfit']}")
            print(f"  Rationale: {data['rationale']}")
            print("  Allocation:")
            for plan in data['cropPlan']:
                print(f"    - {plan['crop']}: {plan['acres']} acres")
                
            if "Mathematical Optimization" not in data.get('rationale', ''):
                print("  ⚠️ WARNING: Rationale indicates fallback might be active?")
        else:
            print(f"❌ Failed: {r.status_code} - {r.text}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    # Ensure server is up (manual step usually, but for script we assume it's running or we run it)
    test_endpoints()
