import sqlite3
import os

DB_PATH = os.path.join('backend', 'aips_project.db')

if not os.path.exists(DB_PATH):
    print(f"Database not found at {DB_PATH}")
else:
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Check tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print("Tables:", [t[0] for t in tables])
        
        # Check combined_dataset
        if ('combined_dataset',) in tables:
            cursor.execute("SELECT COUNT(*) FROM combined_dataset")
            count = cursor.fetchone()[0]
            print(f"Rows in combined_dataset: {count}")
            
            cursor.execute("SELECT DISTINCT Crop FROM combined_dataset LIMIT 10")
            crops = cursor.fetchall()
            print("Sample Crops:", [c[0] for c in crops])
            
            cursor.execute("SELECT DISTINCT Name_of_State FROM combined_dataset LIMIT 10")
            states = cursor.fetchall()
            print("Sample States:", [s[0] for s in states])
        else:
            print("combined_dataset table not found!")
            
        conn.close()
    except Exception as e:
        print(f"Error: {e}")
