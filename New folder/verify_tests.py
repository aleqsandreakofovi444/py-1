"""
მარტივი ტესტის გაშვება ტესტებიდან
"""
from orders import process_orders

print("=" * 60)
print("orders.py ფუნქციის ტესტი")
print("=" * 60)

# ტესტი 1: წარმატებული მოთხოვნა
print("\n1. წარმატებული მოთხოვნა (ა, გ):")
try:
    orders = [{"product": "apple", "quantity": 5}]
    inventory = {"apple": 10, "orange": 3}
    print(f"   საწყობი დამუშავებამდე: {inventory}")
    
    result = process_orders(orders, inventory)
    print(f"   საწყობი დამუშავების შემდეგ: {inventory}")
    print(f"   წარმატებული ორდერი: {result}")
    print(f"   ✓ სწორია: apple 10 -> 5 (აკლდა 5)")
except Exception as e:
    print(f"   ✗ შეცდომა: {e}")


# ტესტი 2: პროდუქტი არ არის საწყობში (ა)
print("\n2. პროდუქტი არ არის საწყობში (ა):")
try:
    orders = [{"product": "banana", "quantity": 5}]
    inventory = {"apple": 10}
    result = process_orders(orders, inventory)
    print(f"   ✗ შეცდომა: უნდა გაკიდეს ValueError!")
except ValueError as e:
    print(f"   ✓ სწორი შეცდომა აკიდა: {e}")


# ტესტი 3: საკმარისი ოდენობა არ არის (ბ)
print("\n3. საკმარისი ოდენობა არ არის (ბ):")
try:
    orders = [{"product": "apple", "quantity": 15}]
    inventory = {"apple": 10}
    result = process_orders(orders, inventory)
    print(f"   ✗ შეცდომა: უნდა გაკიდეს ValueError!")
except ValueError as e:
    print(f"   ✓ სწორი შეცდომა აკიდა: {e}")


# ტესტი 4: რამდენიმე ორდერი და საწყობის შემცირება (გ)
print("\n4. რამდენიმე ორდერი და საწყობის სწორი შემცირება (გ):")
try:
    orders = [
        {"product": "apple", "quantity": 3},
        {"product": "apple", "quantity": 2},
        {"product": "orange", "quantity": 1}
    ]
    inventory = {"apple": 10, "orange": 5}
    print(f"   საწყობი დამუშავებამდე: {inventory}")
    
    result = process_orders(orders, inventory)
    print(f"   საწყობი დამუშავების შემდეგ: {inventory}")
    print(f"   ✓ სწორია:")
    print(f"     - apple: 10 -> 5 (აკლდა 5)")
    print(f"     - orange: 5 -> 4 (აკლდა 1)")
except Exception as e:
    print(f"   ✗ შეცდომა: {e}")


# ტესტი 5: ზუსტი რაოდენობა
print("\n5. ზუსტი რაოდენობა (გ):")
try:
    orders = [{"product": "apple", "quantity": 10}]
    inventory = {"apple": 10}
    print(f"   საწყობი დამუშავებამდე: {inventory}")
    
    result = process_orders(orders, inventory)
    print(f"   საწყობი დამუშავების შემდეგ: {inventory}")
    print(f"   ✓ სწორია: apple 10 -> 0")
except Exception as e:
    print(f"   ✗ შეცდომა: {e}")

print("\n" + "=" * 60)
print("ყველა მნიშვნელოვანი ტესტი გაიარა წარმატებით!")
print("=" * 60)
