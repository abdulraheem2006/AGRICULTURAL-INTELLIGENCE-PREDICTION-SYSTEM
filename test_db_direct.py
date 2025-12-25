import sys
import os

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

# Import database functions
import sqlite3

# Manually test the database query
DATABASE = os.path.join('backend', 'aips_project.db')

print(f"Database path: {DATABASE}")
print(f"Database exists: {os.path.exists(DATABASE)}")

conn = sqlite3.connect(DATABASE)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

query = "SELECT AVG(Yield) as avg_yield, MIN(Yield) as min_yield, MAX(Yield) as max_yield FROM combined_dataset WHERE Crop LIKE ?"
params = ["%Wheat%"]

print(f"\nExecuting query: {query}")
print(f"With params: {params}")

cursor.execute(query, params)
result = cursor.fetchone()

print(f"\nResult type: {type(result)}")
print(f"Result: {result}")

if result:
    print(f"\nTrying to access avg_yield...")
    try:
        avg_yield = result['avg_yield']
        print(f"SUCCESS! avg_yield = {avg_yield}")
        print(f"Type of avg_yield: {type(avg_yield)}")
    except Exception as e:
        print(f"ERROR: {e}")
        print(f"Result has keys method: {hasattr(result, 'keys')}")
        if hasattr(result, 'keys'):
            print(f"Keys: {list(result.keys())}")

conn.close()
