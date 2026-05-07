# Task 3: შემთხვევითი რიცხვების ლისტი (-50-დან 50-მდე) და ლუწი რიცხვების ფილტრაცია (list comprehension)
import random

# 20 ელემენტიანი ლისტი -50-დან 50-მდე შემთხვევითი რიცხვებით (list comprehension)
random_numbers = [random.randint(-50, 50) for _ in range(20)]

# ლუწი რიცხვები (list comprehension)
even_numbers = [num for num in random_numbers if num % 2 == 0]

print("შემთხვევითი რიცხვების ლისტი (20 ელემენტი):")
print(random_numbers)
print("\nლუწი რიცხვები:")
print(even_numbers)
