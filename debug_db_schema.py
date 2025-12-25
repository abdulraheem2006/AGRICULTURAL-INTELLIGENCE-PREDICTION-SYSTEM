import sqlite3
import os

DB_PATH = os.path.join('backend', 'aips_project.db')

def inspect_db():
    if not os.path.exists(DB_PATH):
        print(f"Database not found at {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Get tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables:", [t[0] for t in tables])
    
    # Get users table info
    if ('users',) in tables:
        cursor.execute("PRAGMA table_info(users);")
        columns = cursor.fetchall()
        print("\nUsers table columns:")
        for col in columns:
            print(col)
    else:
        print("\nUsers table does not exist.")
        
    conn.close()

if __name__ == '__main__':
    inspect_db()
