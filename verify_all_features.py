import requests
import json

BASE_URL = "http://localhost:5000/api"

def print_result(title, result):
    print(f"\n--- {title} ---")
    print(json.dumps(result, indent=2))

def verify_crop_prediction():
    print("\n>>> Verifying Crop Prediction Scaling & Sensitivity <<<")
    
    # 1. Scaling Test
    r1 = requests.post(f"{BASE_URL}/predict/yield", json={
        "crop": "Rice", "area": 10, "state": "Punjab", "soilType": "Clay"
    }).json()
    r2 = requests.post(f"{BASE_URL}/predict/yield", json={
        "crop": "Rice", "area": 50, "state": "Punjab", "soilType": "Clay"
    }).json()
    
    yield1 = r1.get('predictedYield', 0)
    yield5 = r2.get('predictedYield', 0)
    
    print(f"10 Acres Yield: {yield1} tons")
    print(f"50 Acres Yield: {yield5} tons")
    
    if 4.8 < yield5 / yield1 < 5.2:
        print("[PASS] Yield scales linearly with Area (approx 5x).")
    else:
        print(f"[FAIL] Scaling mismatch. Ratio: {yield5/yield1 if yield1 else 'N/A'}")

    # 2. Soil Sensitivity Test
    r_sandy = requests.post(f"{BASE_URL}/predict/yield", json={
        "crop": "Rice", "area": 10, "state": "Punjab", "soilType": "Sandy"
    }).json()
    yield_sandy = r_sandy.get('predictedYield', 0)
    
    print(f"10 Acres (Clay): {yield1} tons")
    print(f"10 Acres (Sandy): {yield_sandy} tons")
    
    if yield1 > yield_sandy * 1.3:
        print("[PASS] Soil Sensitivity confirmed (Clay > Sandy for Rice).")
    else:
        print("[FAIL] Soil sensitivity weak or missing.")

def verify_soil_analysis():
    print("\n>>> Verifying Soil Analysis Recommendations <<<")
    
    # 1. Low Nutrient
    r_low = requests.post(f"{BASE_URL}/soil/analyze", json={
        "ph": 6.5, "n": 50, "p": 20, "k": 100
    }).json()
    
    # 2. High/Optimal Nutrient
    r_high = requests.post(f"{BASE_URL}/soil/analyze", json={
        "ph": 6.5, "n": 200, "p": 40, "k": 250
    }).json()
    
    plan_low = r_low.get('action_plan', [])
    plan_high = r_high.get('action_plan', [])
    
    print("Action Plan (Low N/P):", plan_low)
    print("Action Plan (High N/P):", plan_high)
    
    if any("50-60 kg/acre" in s for s in plan_low):
        print("[PASS] Quantitative recommendation found for Low N.")
    else:
        print("[FAIL] detailed recommendation missing for Low N.")
        
    if plan_low != plan_high:
        print("[PASS] Recommendations are dynamic based on input.")
    else:
        print("[FAIL] Action plans are identical.")

def verify_optimization():
    print("\n>>> Verifying Farm Optimization <<<")
    
    # 1. Test Small Water Unit (should be interpreted as m3 and allow full allocation)
    r = requests.post(f"{BASE_URL}/optimize", json={
        "total_area": 10,
        "water_available": 5000, # 5000 m3 = 5ML. Enough for 25 acres of wheat.
        "crops": ["Wheat"]
    }).json()
    
    allocated_acres = 0
    if 'cropPlan' in r and r['cropPlan']:
        allocated_acres = r['cropPlan'][0]['acres']
        
    print(f"Input: 10 Acres, 5000 Water (interpreted as m3)")
    print(f"Allocated: {allocated_acres} Acres")
    
    if allocated_acres == 10:
        print("[PASS] Optimization handled small water unit correctly and allocated full area.")
    else:
        print(f"[FAIL] Allocation constrained. allocated: {allocated_acres}")
        
    # Check proper profit logic
    profit = 0
    if 'summary' in r:
         profit = r['summary'].get('totalProfit', 0)
    print(f"Total Profit: {profit}")
    if profit > 10000:
        print("[PASS] Profit calculation is positive and realistic.")
    else:
        print("[FAIL] Profit is zero or negative.")

if __name__ == "__main__":
    try:
        verify_crop_prediction()
        verify_soil_analysis()
        verify_optimization()
        print("\n=== ALL SYSTEM CHECKS COMPLETED ===")
    except Exception as e:
        print(f"\n[ERROR] Verification failed: {e}")
