import sqlite3
import os

DB_PATH = os.path.join('backend', 'aips_project.db')

def clean_db():
    if not os.path.exists(DB_PATH):
        print(f"Database not found at {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("Checking for negative values...")
    
    # Count negative values
    cursor.execute("SELECT COUNT(*) FROM combined_dataset WHERE Area < 0 OR Production < 0 OR Yield < 0")
    count = cursor.fetchone()[0]
    print(f"Found {count} rows with negative Area, Production, or Yield.")
    
    if count > 0:
        print("Removing invalid rows...")
        cursor.execute("DELETE FROM combined_dataset WHERE Area < 0 OR Production < 0 OR Yield < 0")
        conn.commit()
        print(f"Removed {count} rows.")
    else:
        print("No invalid rows found.")
        
    # Verify
    cursor.execute("SELECT COUNT(*) FROM combined_dataset")
    remaining = cursor.fetchone()[0]
    print(f"Remaining rows: {remaining}")
    
    conn.close()

if __name__ == '__main__':
    clean_db()
