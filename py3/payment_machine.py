

fee = 50
remaining = fee
valid_bills = [5, 10, 20]

print(f"გადასახდელი თანხაა: {fee} ლარი")

while remaining > 0:
    bill = int(input("მოათავსეთ კუპიურა (5, 10, 20): "))

    if bill not in valid_bills:
        print("არავალიდური კუპიურა. გთხოვთ, შეიტანოთ ვალიდური კუპიურა.")
        continue

    remaining -= bill

    if remaining > 0:
        print(f"დარჩენილია გადასახდელი: {remaining} ლარი")
    else:
        change = -remaining
        print(f"გადახდა დასრულდა. თქვენი ხურდაა: {change} ლარი")
