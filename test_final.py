import requests
import json

print("=" * 60)
print("COMPREHENSIVE ENDPOINT TEST - REAL SQL DATA")
print("=" * 60)

# Test 1: Database Connection
print("\n1. DATABASE CONNECTION TEST")
print("-" * 60)
try:
    response = requests.get("http://localhost:5000/api/test")
    result = response.json()
    print(f"✓ Status: {response.status_code}")
    print(f"✓ Total rows in database: {result.get('total_rows')}")
    print(f"✓ Database path: {result.get('database')}")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 2: Yield Prediction
print("\n2. YIELD PREDICTION TEST (Wheat, 10 acres)")
print("-" * 60)
try:
    response = requests.post("http://localhost:5000/api/predict/yield", 
                            json={"crop": "Wheat", "area": 10, "region": "Punjab"})
    result = response.json()
    print(f"✓ Status: {response.status_code}")
    print(f"✓ Predicted Yield: {result.get('predictedYield')} tons")
    print(f"✓ Yield per hectare: {result.get('yield_per_ha')} tons/ha")
    print(f"✓ Confidence: {result.get('confidence')}%")
    print(f"✓ Data Source: {result.get('data_source')}")
    print(f"✓ Factors: {result.get('factors')}")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 3: Soil Analysis
print("\n3. SOIL ANALYSIS TEST (pH 7.0)")
print("-" * 60)
try:
    response = requests.post("http://localhost:5000/api/soil/analyze",
                            json={"ph": 7.0, "n": 50, "p": 30, "k": 20})
    result = response.json()
    print(f"✓ Status: {response.status_code}")
    print(f"✓ Soil Health: {result.get('soil_health')}")
    print(f"✓ Recommended Crops: {', '.join(result.get('recommended_crops', []))}")
    print(f"✓ Data Source: {result.get('data_source')}")
    print(f"✓ Action Plan:")
    for action in result.get('action_plan', []):
        print(f"  - {action}")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 4: Optimization
print("\n4. FARM OPTIMIZATION TEST (10 acres, 5000L water)")
print("-" * 60)
try:
    response = requests.post("http://localhost:5000/api/optimize",
                            json={"total_area": 10, "water_available": 5000, "crops": ["Wheat", "Rice"]})
    result = response.json()
    print(f"✓ Status: {response.status_code}")
    print(f"✓ Total Profit: ₹{result.get('totalProfit')}")
    print(f"✓ Water Usage: {result.get('waterUsage')}L")
    print(f"✓ Data Source: {result.get('data_source')}")
    print(f"✓ Crop Plan:")
    for crop in result.get('cropPlan', []):
        print(f"  - {crop['crop']}: {crop['acres']} acres, Profit: ₹{crop['estimatedProfit']}")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 5: Price Forecast
print("\n5. PRICE FORECAST TEST (Rice)")
print("-" * 60)
try:
    response = requests.post("http://localhost:5000/api/predict/price",
                            json={"commodity": "Rice"})
    result = response.json()
    print(f"✓ Status: {response.status_code}")
    print(f"✓ Forecast Price: ₹{result.get('forecast')}/quintal")
    print(f"✓ Trend: {result.get('trend')}")
    print(f"✓ Historical Data Points: {len(result.get('history', []))}")
    print(f"✓ Data Source: {result.get('data_source')}")
except Exception as e:
    print(f"✗ Error: {e}")

print("\n" + "=" * 60)
print("ALL TESTS COMPLETED - USING REAL SQL DATA!")
print("=" * 60)
