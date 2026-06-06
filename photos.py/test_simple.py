import requests
import json
import time

print("Fetching first 10 photos...")
start = time.time()

photos = []
for i in range(1, 11):
    try:
        response = requests.get(f"https://jsonplaceholder.typicode.com/photos/{i}", timeout=10)
        photos.append(response.json())
        print(f"Fetched photo {i}")
    except Exception as e:
        print(f"Error on {i}: {e}")

print(f"\nFetched {len(photos)} photos")
print(f"Time: {time.time() - start:.2f}s")
print(json.dumps(photos, indent=2)[:500])
