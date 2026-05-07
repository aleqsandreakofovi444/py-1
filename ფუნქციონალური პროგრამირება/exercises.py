# ===== სავარჯიშო 1: Lambda ფუნქცია sorted()-ში =====
print("=" * 50)
print("სავარჯიშო 1: Lambda ფუნქცია sorted()-ში")
print("=" * 50)

# მასში არსებული ელემენტების მეორე ელემენტის მიხედვით დალაგება
tuples_list = [(1, 3), (4, 2), (2, 5)]
sorted_tuples = sorted(tuples_list, key=lambda x: x[1])
print(f"ორიგინალური ლისტი: {tuples_list}")
print(f"დალაგებული ლისტი (მე-2 ელემენტის მიხედვით): {sorted_tuples}")
print()


# ===== სავარჯიშო 2: გაყოფა ერორების დაჭერით =====
print("=" * 50)
print("სავარჯიშო 2: გაყოფა ერორების დაჭერით")
print("=" * 50)

def divide_numbers():
    """
    მომხმარებელს შეაყვანინებს ორ რიცხვს და პირველ რიცხვს გაყოფს მეორე რიცხვზე
    დაჭერილი ერორები: ValueError (არა ინტეჯერი) და ZeroDivisionError (ნულზე გაყოფა)
    """
    try:
        num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
        num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))
        result = num1 / num2
        print(f"შედეგი: {num1} / {num2} = {result}")
        return result
    except ValueError:
        print(" შეცდომა: გთხოვთ შეიყვანოთ მხოლოდ ინტეჯერი (მთელი რიცხვი)")
    except ZeroDivisionError:
        print(" შეცდომა: ნულზე გაყოფა შეუძლებელია!")

# ამ ფუნქციის გამოძახება
# divide_numbers()  # კომენტარში, რადგან ინტერაქტიული

# დემონსტრაციისათვის მაგალითი:
print("ფუნქცია დაწერილია და მზად გამოსახ სკრიპტის ბოლოს")
print()


# ===== სავარჯიშო 3: filter(), map(), sorted(), reduce() =====
print("=" * 50)
print("სავარჯიშო 3: ფუნქციური პროგრამირება")
print("=" * 50)

from functools import reduce

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 15},
    {"name": "Keyboard", "price": 25},
    {"name": "Monitor", "price": 150},
    {"name": "Power", "price": 100},
    {"name": "Pad", "price": 10},
]

print("\nორიგინალური პროდუქტები:")
for product in products:
    print(f"  - {product['name']}: {product['price']}₾")

# 1. filter() - პროდუქტები რომელთა ფასი ნაკლებია 100-ზე
print("\n1. filter() - ფასი < 100:")
filtered_products = list(filter(lambda p: p['price'] < 100, products))
for product in filtered_products:
    print(f"  - {product['name']}: {product['price']}₾")

# 2. map() - ყველა პროდუქტის სახელი და ფასი
print("\n2. map() - პროდუქტების სახელი და ფასი:")
mapped_products = list(map(lambda p: f"{p['name']}: {p['price']}₾", products))
for item in mapped_products:
    print(f"  - {item}")

# 3. sorted() - დალაგება ფასის მიხედვით
print("\n3. sorted() - დალაგება ფასის მიხედვით (ზრდადი):")
sorted_products = sorted(products, key=lambda p: p['price'])
for product in sorted_products:
    print(f"  - {product['name']}: {product['price']}₾")

# 4. reduce() - ყველა ფასების ჯამი
print("\n4. reduce() - ყველა ფასების ჯამი:")
total_price = reduce(lambda sum_val, p: sum_val + p['price'], products, 0)
print(f"  სულ: {total_price}₾")
print()


# ===== სავარჯიშო 4: რეკურსიული ფუნქცია =====
print("=" * 50)
print("სავარჯიშო 4: რეკურსიული ფუნქცია")
print("=" * 50)

def sum_to_n(n):
    """
    რეკურსიული ფუნქცია, რომელიც დააბრუნებს 1-დან n-ის ჩათვლით 
    ყველა რიცხვის ჯამს
    """
    # ბაზის შემთხვევა (recursion base case)
    if n <= 1:
        return 1
    # რეკურსიული შემთხვევა
    return n + sum_to_n(n - 1)

test_numbers = [5, 10, 20]
for num in test_numbers:
    result = sum_to_n(num)
    print(f"sum_to_n({num}) = {result}")
    # მაგ: 1+2+3+4+5 = 15
print()


# ===== დემონსტრაცია: მომხმარებლის ინტერაქციო მაგალითი =====
print("=" * 50)
print("მომხმარებელი ინტერაქციო მაგალითი (სავარჯიშო 2)")
print("=" * 50)
print("\nთუ გსურთ გაყოფა სცადოთ, გამოძახეთ: divide_numbers()")
print("\nსავარჯიშოს შესაბამის კომენტარს ამოშლილი დემო:")

# მკითხაობის ალტერნატივა (სტატიკური მაგალითი)
try:
    print("\nცდა 1: 10 გაყოფილი 2-ზე:")
    result = 10 / 2
    print(f"  შედეგი: {result}")
except ZeroDivisionError:
    print("   ნულზე გაყოფა შეუძლებელია!")

try:
    print("\nცდა 2: 15 გაყოფილი 0-ზე:")
    result = 15 / 0
    print(f"  შედეგი: {result}")
except ZeroDivisionError:
    print("   ნულზე გაყოფა შეუძლებელია!")

print("\n" + "=" * 50)
print("ყველა სავარჯიშო დასრულებული!")
print("=" * 50)
