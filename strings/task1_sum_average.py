# Task 1: მთელი რიცხვების ჯამი და საშუალო (უჩაშენებელი functions გარეშე)
numbers = [10, 25, 15, 30, 20, 35]

# ჯამის გამოთვლა ციკლის საშუალებით
total_sum = 0
for num in numbers:
    total_sum = total_sum + num

# საშუალოს გამოთვლა
count = 0
for num in numbers:
    count = count + 1

average = total_sum / count

print("ლისტი:", numbers)
print("ჯამი:", total_sum)
print("საშუალო:", average)
