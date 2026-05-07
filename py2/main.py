def bmi_program():
    weight = float(input("შეიყვანეთ წონა (კგ): "))
    height = float(input("შეიყვანეთ სიმაღლე (მ): "))

    if height == 0:
        print("სიმაღლე 0 ვერ იქნება")
        return

    bmi = weight / (height ** 2)
    print(f"BMI = {bmi:.2f}")

    if bmi < 19:
        print("underweight")
    elif 19 <= bmi <= 25:
        print("normalweight")
    else:
        print("overweight")


def calculator_program():
    num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
    num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
    op = input("შეიყვანეთ ოპერატორი (+, -, *, /): ")

    if op == "+":
        print("შედეგი:", num1 + num2)
    elif op == "-":
        print("შედეგი:", num1 - num2)
    elif op == "*":
        print("შედეგი:", num1 * num2)
    elif op == "/":
        if num2 == 0:
            print("0-ზე გაყოფა არ შეიძლება")
        else:
            print("შედეგი:", num1 / num2)
    else:
        print("არასწორი ოპერატორი")


def max_of_three_program():
    a = float(input("შეიყვანეთ პირველი რიცხვი: "))
    b = float(input("შეიყვანეთ მეორე რიცხვი: "))
    c = float(input("შეიყვანეთ მესამე რიცხვი: "))

    if a == b or a == c or b == c:
        print("შეიყვანეთ განსხვავებული რიცხვები")
    else:
        print("ყველაზე დიდი რიცხვია:", max(a, b, c))


def main():
    print("=== 1) BMI გამოთვლა ===")
    bmi_program()
    print()

    print("=== 2) კალკულატორი ===")
    calculator_program()
    print()

    print("=== 3) 3 რიცხვიდან ყველაზე დიდი ===")
    max_of_three_program()


if __name__ == "__main__":
    main()
