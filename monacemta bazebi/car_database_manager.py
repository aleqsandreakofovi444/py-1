#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ავტომანქანების მონაცემთა ბაზის ოპერაციები
Car Database Operations with SQLite
"""

import sqlite3
from tabulate import tabulate
import os

# Database file
DB_FILE = 'cars.db'

def init_database():
    """ცხრილის შექმნა და მონაცემთა ჩამატება"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # ცხრილის შექმნა
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER NOT NULL,
            price REAL NOT NULL,
            is_sold INTEGER DEFAULT 0,
            is_registered INTEGER DEFAULT 1
        )
    ''')
    
    # ძველი მონაცემის წაშლა (თუ ცხრილი უკვე არსებობდა)
    cursor.execute('DELETE FROM cars')
    
    # ნიმუშის მონაცემი
    sample_data = [
        ('Toyota', 'Corolla', 2015, 8000, 0, 1),
        ('BMW', 'X5', 2018, 45000, 0, 1),
        ('Mercedes', 'E-Class', 2012, 15000, 1, 1),
        ('Audi', 'A4', 2010, 12000, 0, 0),
        ('Honda', 'Civic', 2016, 10000, 1, 1),
        ('Volkswagen', 'Golf', 2014, 7500, 0, 1),
        ('Ford', 'Focus', 2011, 5000, 0, 0),
        ('Mazda', 'CX-5', 2017, 18000, 0, 1),
        ('Toyota', 'Camry', 2019, 22000, 0, 1),
        ('Tesla', 'Model 3', 2020, 35000, 0, 1),
    ]
    
    cursor.executemany(
        'INSERT INTO cars (brand, model, year, price, is_sold, is_registered) VALUES (?, ?, ?, ?, ?, ?)',
        sample_data
    )
    
    conn.commit()
    conn.close()
    print("✓ მონაცემთა ბაზა ინიციალიზებულია (Database initialized)")
    print()

def print_result(title, columns, data):
    """შედეგის დაბეჭდვა"""
    print(f"\n{'='*70}")
    print(f"📋 {title}")
    print(f"{'='*70}")
    if data:
        print(tabulate(data, headers=columns, tablefmt="grid"))
        print(f"სულ ჩანაწერი: {len(data)} (Total records: {len(data)})")
    else:
        print("❌ ჩანაწერი არ მოიძებნა (No records found)")
    print()

def query_all():
    """2.1 გამოიტანეთ ყველა მონაცემის ყველა სვეტი"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cars')
    result = cursor.fetchall()
    conn.close()
    
    columns = ['ID', 'ბრენდი', 'მოდელი', 'წელი', 'ფასი', 'გაყიდული', 'განბაჟებული']
    print_result("ყველა მონაცემის ყველა სვეტი (All columns of all data)", columns, result)

def query_specific_columns():
    """2.2 გამოიტანეთ ყველა ავტომანქანა განსაზღვრული სვეტებით"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT brand, model, year, price FROM cars')
    result = cursor.fetchall()
    conn.close()
    
    columns = ['ბრენდი', 'მოდელი', 'წელი', 'ფასი']
    print_result("ავტომანქანები: ბრენდი, მოდელი, წელი, ფასი", columns, result)

def query_by_brand(brand='Toyota'):
    """2.3 გამოიტანეთ ყველა ავტომანქანა კონკრეტული ბრენდის მიხედვით"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cars WHERE brand = ?', (brand,))
    result = cursor.fetchall()
    conn.close()
    
    columns = ['ID', 'ბრენდი', 'მოდელი', 'წელი', 'ფასი', 'გაყიდული', 'განბაჟებული']
    print_result(f"ყველა ავტომანქანა: {brand}", columns, result)

def query_price_range():
    """2.4 გამოიტანეთ ყველა ავტომანქანა რომლის ფასი 2000-5000 შორის"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cars WHERE price BETWEEN 2000 AND 5000')
    result = cursor.fetchall()
    conn.close()
    
    columns = ['ID', 'ბრენდი', 'მოდელი', 'წელი', 'ფასი', 'გაყიდული', 'განბაჟებული']
    print_result("ავტომანქანები: ფასი 2000-5000 შორის", columns, result)

def query_year_and_registered():
    """2.5 გამოიტანეთ ყველა ავტომანქანა 2010+ წელი და განბაჟებული"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cars WHERE year >= 2010 AND is_registered = 1')
    result = cursor.fetchall()
    conn.close()
    
    columns = ['ID', 'ბრენდი', 'მოდელი', 'წელი', 'ფასი', 'გაყიდული', 'განბაჟებული']
    print_result("ავტომანქანები: წელი 2010+ და განბაჟებული", columns, result)

def query_sold_cars():
    """დამატებითი: გაყიდული ავტომანქანები"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cars WHERE is_sold = 1')
    result = cursor.fetchall()
    conn.close()
    
    columns = ['ID', 'ბრენდი', 'მოდელი', 'წელი', 'ფასი', 'გაყიდული', 'განბაჟებული']
    print_result("გაყიდული ავტომანქანები (Sold cars)", columns, result)

def query_price_by_brand():
    """დამატებითი: საშუალო ფასი ბრენდის მიხედვით"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT brand, COUNT(*) as count, AVG(price) as avg_price, 
               MIN(price) as min_price, MAX(price) as max_price 
        FROM cars GROUP BY brand ORDER BY avg_price DESC
    ''')
    result = cursor.fetchall()
    conn.close()
    
    columns = ['ბრენდი', 'რაოდენობა', 'საშუალო ფასი', 'მინ. ფასი', 'მაქს. ფასი']
    print_result("საშუალო ფასი ბრენდის მიხედვით", columns, result)

def delete_first_two():
    """3.1 წაშალეთ პირველი ორი მონაცემი აიდის მიხედვით"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM cars WHERE id IN (1, 2)')
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    
    print(f"✓ წაშლილია {affected} ჩანაწერი (Deleted {affected} records)")

def delete_sold_cars():
    """3.2 წაშალეთ ყველა გაყიდული ავტომანქანა"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM cars WHERE is_sold = 1')
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    
    print(f"✓ წაშლილია {affected} გაყიდული ავტომანქანა (Deleted {affected} sold cars)")

def delete_all_data():
    """3.3 წაშალეთ ყველა მონაცემი"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM cars')
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    
    print(f"✓ წაშლილია ყველა მონაცემი - {affected} ჩანაწერი (Deleted all {affected} records)")

def truncate_table():
    """3.4 გაასუფთავეთ ცხრილი"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM cars')  # SQLite-ში TRUNCATE-ის ნაცვლად DELETE
    conn.commit()
    conn.close()
    
    print("✓ ცხრილი გაასუფთავა (Table cleared)")

def drop_table():
    """3.5 წაშალეთ ცხრილი"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS cars')
    conn.commit()
    conn.close()
    
    print("✓ ცხრილი წაშლილია (Table dropped)")

def show_menu():
    """მენიუ"""
    print("\n" + "="*70)
    print("🚗 ავტომანქანების მონაცემთა ბაზის ოპერაციები")
    print("   CAR DATABASE OPERATIONS")
    print("="*70)
    print("\n📊 მონაცემთა გამოტანა (SELECT OPERATIONS):")
    print("  1. ყველა მონაცემის ყველა სვეტი")
    print("  2. სპეციფიკური სვეტები (ბრენდი, მოდელი, წელი, ფასი)")
    print("  3. კონკრეტული ბრენდის ავტომანქანები")
    print("  4. ფასი 2000-5000 შორის")
    print("  5. წელი 2010+ და განბაჟებული")
    print("  6. გაყიდული ავტომანქანები")
    print("  7. საშუალო ფასი ბრენდის მიხედვით")
    
    print("\n🗑️  მონაცემთა წაშლა (DELETE OPERATIONS):")
    print("  8. პირველი ორი მონაცემი (ID 1,2)")
    print("  9. ყველა გაყიდული ავტომანქანა")
    print("  10. ყველა მონაცემი (DELETE FROM)")
    print("  11. ცხრილი გაასუფთავა (TRUNCATE)")
    print("  12. ცხრილი წაშლა (DROP)")
    
    print("\n🔧 სხვა ოპერაციები (OTHER):")
    print("  0. გამოსვლა (Exit)")
    print("="*70)

def main():
    """მთავარი ფუნქცია"""
    # ბაზის ინიციალიზაცია
    init_database()
    
    while True:
        show_menu()
        choice = input("\n აირჩიეთ ოპერაცია (Select operation): ").strip()
        
        try:
            if choice == '1':
                query_all()
            elif choice == '2':
                query_specific_columns()
            elif choice == '3':
                brand = input("ბრენდის სახელი (Brand name): ").strip()
                query_by_brand(brand if brand else 'Toyota')
            elif choice == '4':
                query_price_range()
            elif choice == '5':
                query_year_and_registered()
            elif choice == '6':
                query_sold_cars()
            elif choice == '7':
                query_price_by_brand()
            elif choice == '8':
                confirm = input("დასტურდება პირველი ორი მონაცემის წაშლა? (Confirm deletion of first 2 records?) (y/n): ").lower()
                if confirm == 'y':
                    delete_first_two()
            elif choice == '9':
                confirm = input("დასტურდება ყველა გაყიდული ავტომანქანის წაშლა? (Confirm deletion of sold cars?) (y/n): ").lower()
                if confirm == 'y':
                    delete_sold_cars()
            elif choice == '10':
                confirm = input("დასტურდება ყველა მონაცემის წაშლა? (Confirm deletion of all data?) (y/n): ").lower()
                if confirm == 'y':
                    delete_all_data()
            elif choice == '11':
                confirm = input("დასტურდება ცხრილის გასუფთავება? (Confirm truncation?) (y/n): ").lower()
                if confirm == 'y':
                    truncate_table()
            elif choice == '12':
                confirm = input("დასტურდება ცხრილის წაშლა? (Confirm table drop?) (y/n): ").lower()
                if confirm == 'y':
                    drop_table()
                    init_database()  # ცხრილის აღდგენა
            elif choice == '0':
                print("\n👋 გამოვედით (Goodbye!)")
                break
            else:
                print("❌ არასწორი ყველაზე (Invalid option)")
                
        except Exception as e:
            print(f"❌ შეცდომა: {e}")

if __name__ == '__main__':
    main()
