import sqlite3

# ბაზის გამომკითხველი სკრიპტი
# Database query utility

def print_table(headers, rows):
    """მარტივი ცხრილის ბეჭდვა"""
    # სვეტის სიგანე
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))
    
    # თავი
    header_line = " | ".join(str(h).ljust(col_widths[i]) for i, h in enumerate(headers))
    print(header_line)
    print("-" * len(header_line))
    
    # რიგები
    for row in rows:
        print(" | ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row)))

def display_all_cars():
    """ყველა მანქანის ჩვენება"""
    conn = sqlite3.connect('cars.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM cars ORDER BY car_id')
    rows = cursor.fetchall()
    
    if not rows:
        print("მონაცემი ვერ იპოვა")
        return
    
    headers = ['ID', 'ბრენდი', 'მოდელი', 'წელი', 'VIN', 'ძრ.მოც.', 'გარბენი', 'განბაჟ', 'ფასი', 'გაყიდ']
    
    # მონაცემების ფორმატირება
    formatted_rows = []
    for row in rows:
        formatted_row = [
            row[0],  # ID
            row[1],  # ბრენდი
            row[2],  # მოდელი
            row[3],  # წელი
            row[4][:8] if row[4] else '-',  # VIN კოდი (შემოკლებული)
            row[6],  # ძრ.მოც.
            row[7] if row[7] else '-',  # გარბენი
            'კი' if row[8] else 'არა',  # განბაჟ
            f"{row[9]:.2f}" if row[9] else '-',  # ფასი
            'გაყიდ' if row[11] else 'ხელმ'  # გაყიდ
        ]
        formatted_rows.append(formatted_row)
    
    print("\n📋 ავტომობილების სრული ლისტი:")
    print_table(headers, formatted_rows)
    
    conn.close()


def search_by_brand(brand):
    """მოძიება ბრენდის მიხედვით"""
    conn = sqlite3.connect('cars.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM cars WHERE brand LIKE ? ORDER BY car_id', (f'%{brand}%',))
    rows = cursor.fetchall()
    
    if not rows:
        print(f"მოძიება '{brand}' ბრენდის - შედეგი ვერ იპოვა")
        return
    
    headers = ['ID', 'ბრენდი', 'მოდელი', 'წელი', 'ფასი', 'გარბენი', 'განბაჟ', 'გაყიდ']
    print(f"\n🔍 ძებნის შედეგი '{brand}'ის მიხედვით ({len(rows)} შედეგი):")
    
    formatted_rows = [[row[0], row[1], row[2], row[3], f"{row[9]:.2f}" if row[9] else '-', row[7], 'კი' if row[8] else 'არა', 'გაყიდ' if row[11] else 'ხელმ'] for row in rows]
    print_table(headers, formatted_rows)
    
    conn.close()

def get_statistics():
    """სტატისტიკა"""
    conn = sqlite3.connect('cars.db')
    cursor = conn.cursor()
    
    # საერთო რაოდენობა
    cursor.execute('SELECT COUNT(*) FROM cars')
    total = cursor.fetchone()[0]
    
    # გაყიდული
    cursor.execute('SELECT COUNT(*) FROM cars WHERE is_sold = 1')
    sold = cursor.fetchone()[0]
    
    # ხელმისაწვდომელი
    cursor.execute('SELECT COUNT(*) FROM cars WHERE is_sold = 0')
    available = cursor.fetchone()[0]
    
    # საშუალო ფასი
    cursor.execute('SELECT AVG(price) FROM cars WHERE price IS NOT NULL')
    avg_price = cursor.fetchone()[0] or 0
    
    # საშუალო ძრ.მოცულობა
    cursor.execute('SELECT AVG(engine_volume) FROM cars')
    avg_engine = cursor.fetchone()[0] or 0
    
    # საშუალო გარბენი
    cursor.execute('SELECT AVG(mileage_km) FROM cars WHERE mileage_km IS NOT NULL')
    avg_mileage = cursor.fetchone()[0] or 0
    
    print("\n📊 სტატისტიკა:")
    print(f"  • საერთო ავტომობილი: {total}")
    print(f"  • გაყიდული: {sold}")
    print(f"  • ხელმისაწვდომელი: {available}")
    print(f"  • საშუალო ფასი: {avg_price:.2f}")
    print(f"  • საშუალო ძრავის მოცულობა: {avg_engine:.2f}")
    print(f"  • საშუალო გარბენი: {avg_mileage:.0f} კმ")
    
    conn.close()

if __name__ == '__main__':
    print("=" * 80)
    print("🚗 ავტომობილების ბაზის ის გამომკითხველი")
    print("=" * 80)
    
    display_all_cars()
    get_statistics()
    
    # მაგალითი: ძებნა
    # search_by_brand('Toyota')
