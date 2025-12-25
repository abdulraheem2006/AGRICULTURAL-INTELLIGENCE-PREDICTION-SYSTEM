import sys
sys.path.append('backend')
from database.db import get_crop_yield_stats, get_price_history

# Test the exact functions being called
print("Testing get_crop_yield_stats...")
result = get_crop_yield_stats('Wheat', None)
print(f"Type: {type(result)}")
print(f"Result: {result}")

if result:
    print(f"\nTrying to access avg_yield...")
    try:
        avg_yield = result['avg_yield']
        print(f"Success! avg_yield = {avg_yield}")
    except Exception as e:
        print(f"Error: {e}")
        print(f"Result keys: {result.keys() if hasattr(result, 'keys') else 'No keys method'}")

print("\n\nTesting get_price_history...")
price_data = get_price_history('Wheat')
print(f"Type: {type(price_data)}")
print(f"Length: {len(price_data) if price_data else 0}")
if price_data and len(price_data) > 0:
    print(f"First row type: {type(price_data[0])}")
    print(f"First row: {price_data[0]}")
    try:
        price = price_data[0]['Modal_Price']
        print(f"Success! price = {price}")
    except Exception as e:
        print(f"Error: {e}")
