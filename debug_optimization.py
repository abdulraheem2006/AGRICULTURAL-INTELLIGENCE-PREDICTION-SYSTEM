
import sqlite3
import os
import sys

# Adjust path to find backend
sys.path.append(os.path.join(os.getcwd(), 'backend'))

from backend.models.milp_model import MILPOptimizer

DB_PATH = 'backend/aips_project.db'

def check_data():
    if not os.path.exists(DB_PATH):
        print(f"Error: DB not found at {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    crops = ['Wheat', 'Rice', 'Maize', 'Sugarcane']
    print(f"Checking data for crops: {crops}")
    
    crops_data = []
    
    for crop in crops:
        cursor.execute("SELECT AVG(Yield) as avg_yield FROM combined_dataset WHERE Crop LIKE ?", [f"%{crop}%"])
        row = cursor.fetchone()
        yld = row[0] if row else None
        
        cursor.execute("SELECT AVG(Modal_Price) as avg_price FROM combined_dataset WHERE Commodity LIKE ?", [f"%{crop}%"])
        row2 = cursor.fetchone()
        price = row2[0] if row2 else None
        
        print(f"Crop: {crop}, Yield: {yld}, Price: {price}")
        
        if yld:
             # Logic from app.py
            avg_yield = float(yld)
            avg_price = float(price) if price else 2000
            
            profit = (avg_yield * (avg_price/100)) - 5000
            crops_data.append({
                'name': crop,
                'profit_per_acre': profit,
                'water_per_acre': 200000 # Dummy
            })

    conn.close()
    
    print("\nCrops Data Prepared:", crops_data)
    
    if not crops_data:
        print("NO VALID CROP DATA FOUND!")
        return

    optimizer = MILPOptimizer()
    print("\nRunning Optimization...")
    try:
        result = optimizer.optimize_farm(10, 500000, crops_data)
        print("Result:", result)
    except Exception as e:
        print("Optimization Exception:", e)

if __name__ == "__main__":
    check_data()
