import sqlite3
from datetime import datetime

# ბაზის შესაქმნელი სკრიპტი
# Database creation script for cars

def create_database():
    # SQLite ბაზასთან დაკავშირება/ბაზის შექმნა
    conn = sqlite3.connect('cars.db')
    cursor = conn.cursor()
    
    # ცხრილის შექმნა
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand VARCHAR(100) NOT NULL,
            model VARCHAR(100) NOT NULL,
            year INTEGER NOT NULL,
            vin_code VARCHAR(17) UNIQUE,
            added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            engine_volume DECIMAL(5,2) CHECK(engine_volume > 0.5),
            mileage_km INTEGER,
            is_cleared BOOLEAN DEFAULT 0,
            price DECIMAL(10,2),
            description TEXT,
            is_sold BOOLEAN DEFAULT 0
        )
    ''')
    
    # ცხრილის გასუფთავება (ხელახლა გაშვების შემთხვევაში)
    cursor.execute('DELETE FROM cars')
    
    # მონაცემების შეტანა
    cars_data = [
        ('Toyota', 'Camry', 2022, 'JTDBRFK30D2123456', 2.5, 15000, 1, 25000.00, 'თეთრი სუფთა ავტომობილი, პერფექტური მდგომარეობით', 0),
        ('BMW', 'X5', 2021, 'WBXYZ1234567890AB', 3.0, 25000, 1, 45000.50, 'ძლევა დიდი, მოდერნული ტექნოლოგიები', 0),
        ('Mercedes-Benz', 'C-Class', 2020, 'WDDZH4GB6LF123456', 2.0, 40000, 0, 35000.00, 'ღირსეული, კარგი მდგომარეობა', 1),
        ('Audi', 'A4', 2023, 'WAUZZZ8K3NA123456', 1.8, 5000, 1, 38000.75, 'ახალი, პირველი მფლობელი, მუქი სახლის ფერი', 0),
        ('Volkswagen', 'Passat', 2019, 'WVWZZZ3CZ9E123456', 1.6, 60000, 0, 18000.00, 'ეკონომიური გარბენისა და ხარჯებით', 0),
        ('Honda', 'Civic', 2021, 'JHMFC7F37MU123456', 1.5, 35000, 1, 20000.00, 'საიმედო მანქანა, ჯანმრთელი სვეტი', 0),
        ('Ford', 'Mustang', 2022, '1FA6P8TH7N5123456', 3.7, 12000, 1, 50000.99, 'სპორტული, მძლავრი ძრავი, წითელი ფერი', 0),
        ('Skoda', 'Octavia', 2020, 'TMAUZZZ8K3NA123456', 1.4, 55000, 0, 16000.50, 'დაზიანებული წინა ნაწილი, გასასწორებელი', 1),
        ('Hyundai', 'Elantra', 2023, 'KMHEC4A46NU123456', 1.6, 8000, 1, 19000.00, 'ახალი, იაფი, ოჯახის მანქანა', 0),
        ('Kia', 'Sportage', 2021, 'KNDPM3AC1L7123456', 2.0, 42000, 0, 22000.25, 'კომფორტული SUV, ოჯახის მანქანა', 0),
        ('Mazda', 'CX-5', 2022, 'JM1BL1UJ8F0123456', 2.5, 18000, 1, 28000.75, 'დინამიური და ეკონომიური', 0),
        ('Subaru', 'Outback', 2020, 'JF1BR6SA9L5123456', 2.5, 50000, 0, 26000.00, 'AWD სისტემით, მუქი ფერი, ყველა პირობისთვის', 0),
    ]
    
    # მონაცემების ჩასმა
    for car in cars_data:
        cursor.execute('''
            INSERT INTO cars (brand, model, year, vin_code, engine_volume, mileage_km, 
                            is_cleared, price, description, is_sold)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', car)
    
    conn.commit()
    
    # შედეგების ჩვენება
    cursor.execute('SELECT COUNT(*) FROM cars')
    count = cursor.fetchone()[0]
    print(f"✓ ბაზა წარმატებით შეიქმნა!")
    print(f"✓ მონაცემი დაემატა: {count} ავტომობილი")
    print("\n📋 ყველა მონაცემი:")
    print("-" * 120)
    
    # ყველა მანქანის ჩვენება
    cursor.execute('SELECT * FROM cars')
    columns = [description[0] for description in cursor.description]
    
    # თავი
    print(f"{'ID':<4} {'ბრენდი':<15} {'მოდელი':<15} {'წელი':<6} {'ძრ.მოცული':<10} {'გარბენი':<8} {'განბაჟ':<7} {'ფასი':<12} {'გაყიდ':<6}")
    print("-" * 120)
    
    for row in cursor.fetchall():
        print(f"{row[0]:<4} {row[1]:<15} {row[2]:<15} {row[3]:<6} {str(row[6]):<10} {str(row[7] or '-'):<8} {'კი' if row[8] else 'არა':<7} {str(row[9]) if row[9] else '-':<12} {'გაყიდ' if row[11] else 'ხელმისაწ':<6}")
    
    print("\n✓ ბაზა წარმატებით უშინდებელია!")
    
    conn.close()

if __name__ == '__main__':
    create_database()
