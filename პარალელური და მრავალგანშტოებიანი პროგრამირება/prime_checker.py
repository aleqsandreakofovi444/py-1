import threading
from typing import List, Dict

# ფუნქცია რომელიც შეამოწმებს არის თუ არა რიცხვი მარტივი
def is_prime(num: int) -> bool:
    """
    შეამოწმებს არის თუ არა რიცხვი მარტივი
    """
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# შედეგების შენახვისათვის
results = {}
results_lock = threading.Lock()

def check_prime_threaded(num: int) -> None:
    """
    ფუნქცია რომელიც ნაკადზე ეშვება
    """
    prime_status = is_prime(num)
    with results_lock:
        results[num] = prime_status

# რიცხვების ლისტი
num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51]

# ნაკადების შექმნა და ეშვება
threads = []
for num in num_list:
    thread = threading.Thread(target=check_prime_threaded, args=(num,))
    threads.append(thread)
    thread.start()

# ყველა ნაკადის დასრულების ლოდინი
for thread in threads:
    thread.join()

# შედეგების დაბეჭდვა
print("რიცხვი | მარტივი თუ არა")
print("-" * 30)
for num in num_list:
    status = "მარტივი ✓" if results[num] else "არ არის მარტივი ✗"
    print(f"{num:3d}   | {status}")

# სულ მარტივი რიცხვების რაოდენობა
prime_count = sum(1 for v in results.values() if v)
print("-" * 30)
print(f"სულ მარტივი რიცხვი: {prime_count} / {len(num_list)}")
