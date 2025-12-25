import sqlite3
import os
import requests
import json

# DB Path
DB_PATH = os.path.join('backend', 'aips_project.db')

def debug_data():
    print("--- Checking Database Data ---")
    if not os.path.exists(DB_PATH):
        print(f"Error: DB not found at {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    crops = ['Wheat', 'Rice', 'Maize', 'Sugarcane', 'Cotton', 'Potato']
    
    print(f"{'Crop':<12} | {'Yield':<10} | {'Price':<10} | {'Est. Profit/Acre':<15}")
    print("-" * 60)
    
    for crop in crops:
        # Get yield
        cursor.execute("SELECT AVG(Yield) as avg_yield FROM combined_dataset WHERE Crop LIKE ?", [f"%{crop}%"])
        yield_res = cursor.fetchone()
        avg_yield = float(yield_res['avg_yield']) if yield_res and yield_res['avg_yield'] else 0
        
        # Get price
        cursor.execute("SELECT AVG(Modal_Price) as avg_price FROM combined_dataset WHERE Commodity LIKE ?", [f"%{crop}%"])
        price_res = cursor.fetchone()
        avg_price = float(price_res['avg_price']) if price_res and price_res['avg_price'] else 2000
        
        # Calculate Profit as per app.py logic
        # profit_per_acre = (avg_yield * (avg_price/100)) - 5000 
        profit = (avg_yield * (avg_price / 100)) - 5000
        
        print(f"{crop:<12} | {avg_yield:<10.2f} | {avg_price:<10.2f} | {profit:<15.2f}")
        
    conn.close()

def debug_api():
    print("\n--- Checking API Response ---")
    try:
        payload = {
            "total_area": 10,
            "water_available": 100000, 
            "crops": ['Wheat', 'Rice', 'Maize']
        }
        r = requests.post("http://localhost:5000/api/optimize", json=payload)
        if r.status_code == 200:
            print(json.dumps(r.json(), indent=2))
        else:
            print(f"Error: {r.status_code} - {r.text}")
    except Exception as e:
        print(f"Requests Error: {e}")

if __name__ == "__main__":
    debug_data()
    debug_api()
