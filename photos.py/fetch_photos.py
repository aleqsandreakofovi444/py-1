import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import time

BASE_URL = "https://jsonplaceholder.typicode.com/photos"
TOTAL_PHOTOS = 5000


def fetch_photo(photo_id):
    """Fetches a single photo by ID and returns the JSON data"""
    max_retries = 3
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            url = f"{BASE_URL}/{photo_id}"
            response = requests.get(url, timeout=15)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            retry_count += 1
            if retry_count < max_retries:
                time.sleep(0.5)


def main():
    print(f"Starting to fetch {TOTAL_PHOTOS} photos...")
    start_time = time.time()
    
    max_workers = 15
    
    photos = {}
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures_map = {executor.submit(fetch_photo, photo_id): photo_id 
                      for photo_id in range(1, TOTAL_PHOTOS + 1)}
        
        completed = 0
        failed = 0
        
        for future in as_completed(futures_map):
            try:
                photo_data = future.result()
                photo_id = futures_map[future]
                
                if photo_data:
                    photos[photo_data['id']] = photo_data
                    completed += 1
                else:
                    failed += 1
                
                if (completed + failed) % 500 == 0:
                    elapsed = time.time() - start_time
                    print(f"Processed {completed + failed} photos ({completed} success, {failed} failed) in {elapsed:.1f}s...")
            except Exception as e:
                failed += 1
    
    sorted_photos = [photos[i] for i in range(1, TOTAL_PHOTOS + 1) if i in photos]
    
    with open("photos.json", "w", encoding="utf-8") as f:
        json.dump(sorted_photos, f, indent=2, ensure_ascii=False)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    print(f"\n{'='*60}")
    print(f"SUCCESS! Fetched and saved {len(sorted_photos)} out of {TOTAL_PHOTOS} photos")
    print(f"Failed/Skipped: {TOTAL_PHOTOS - len(sorted_photos)} photos")
    print(f"Saved to: photos.json")
    print(f"Total execution time: {execution_time:.2f} seconds")
    if len(sorted_photos) > 0:
        print(f"Average time per photo: {(execution_time / len(sorted_photos)) * 1000:.2f} ms")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
