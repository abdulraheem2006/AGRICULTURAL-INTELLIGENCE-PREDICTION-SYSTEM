
import requests
import json
import time
import sys

# Force unbuffered output
sys.stdout.reconfigure(line_buffering=True)

url = "http://localhost:5000/api/predict/yield"

test_cases = [
    {
        "crop": "Wheat", "area": 10, "rainfall": 1000, "fertilizer": 120, "pesticide": 40, "region": "Punjab"
    },
    {
        "crop": "Rice", "area": 5, "rainfall": 2000, "fertilizer": 150, "pesticide": 60, "region": "West Bengal"
    }
]

with open("test_output.txt", "w") as f:
    f.write("Starting Test...\n")
    print("Starting Test...")
    
    for i, data in enumerate(test_cases):
        try:
            print(f"Requesting case {i+1}...")
            f.write(f"Requesting case {i+1}...\n")
            
            response = requests.post(url, json=data, timeout=5)
            
            f.write(f"Status: {response.status_code}\n")
            print(f"Status: {response.status_code}")
            
            if response.status_code == 200:
                res = response.json()
                msg = f"Case {i+1}: Conf={res.get('confidence')}%"
                print(msg)
                f.write(msg + "\n")
            else:
                msg = f"Case {i+1} Failed: {response.text}"
                print(msg)
                f.write(msg + "\n")
                
        except Exception as e:
            msg = f"Error case {i+1}: {e}"
            print(msg)
            f.write(msg + "\n")
        
        print("-" * 30)
        f.write("-" * 30 + "\n")

    f.write("Done.\n")
    print("Done.")
