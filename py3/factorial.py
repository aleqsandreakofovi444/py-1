

number = int(input("შეიყვანეთ რიცხვი: "))

if number < 0:
    print("უარყოფითი რიცხვის ფაქტორიალი არ განისაზღვრება.")
else:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i

    print(f"{number}-ის ფაქტორიალია: {factorial}")
