import sqlite3
import os

DB_PATH = os.path.join('backend', 'aips_project.db')

def check_data():
    if not os.path.exists(DB_PATH):
        print(f"Database not found at {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    print("-" * 20)
    print("Checking for 'Wheat'...")
    cursor.execute("SELECT count(*) FROM combined_dataset WHERE Crop LIKE '%Wheat%'")
    print(f"Count: {cursor.fetchone()[0]}")
    
    print("-" * 20)
    print("Checking for 'PUNJAB'...")
    cursor.execute("SELECT count(*) FROM combined_dataset WHERE Name_of_State LIKE '%PUNJAB%'")
    print(f"Count: {cursor.fetchone()[0]}")

    print("-" * 20)
    print("Sample Data (First 3 rows):")
    cursor.execute("SELECT Crop, Name_of_State, Yield FROM combined_dataset LIMIT 3")
    for row in cursor.fetchall():
        print(dict(row))

    conn.close()

if __name__ == "__main__":
    check_data()
