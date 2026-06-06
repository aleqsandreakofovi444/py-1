import requests

# Test if API is accessible
try:
    print("Testing API connection...")
    response = requests.get("https://jsonplaceholder.typicode.com/photos/1", timeout=15)
    print(f"Status code: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")
