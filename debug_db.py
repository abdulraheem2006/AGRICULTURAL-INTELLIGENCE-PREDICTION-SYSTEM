import sqlite3
import sys
sys.path.append('backend')

DATABASE = 'backend/aips_project.db'

def test_query():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    query = "SELECT AVG(Yield) as avg_yield, MIN(Yield) as min_yield, MAX(Yield) as max_yield FROM combined_dataset WHERE Crop LIKE ?"
    cursor.execute(query, ["%Wheat%"])
    result = cursor.fetchone()
    
    print(f"Result type: {type(result)}")
    print(f"Result: {result}")
    
    if result:
        print(f"avg_yield type: {type(result['avg_yield'])}")
        print(f"avg_yield value: {result['avg_yield']}")
        print(f"Keys: {result.keys()}")
    
    conn.close()

test_query()
