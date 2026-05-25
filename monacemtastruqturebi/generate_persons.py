import csv
from faker import Faker

# Faker-ის ინიციალიზაცია
fake = Faker()

# CSV ფაილის ქმნა და 50 პიროვნების ჩამატება
with open('persons.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['ID', 'first_name', 'last_name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Header-ის ჩამატება
    writer.writeheader()
    
    # 50 ფიქტიური პიროვნის გენერაცია
    for i in range(1, 51):
        writer.writerow({
            'ID': i,
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'age': fake.random_int(min=20, max=80)
        })

print("✓ persons.csv ფაილი წარმატებით შეიქმნა 50 პიროვნით!")
