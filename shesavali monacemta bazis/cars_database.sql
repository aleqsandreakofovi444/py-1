-- ავტომობილების ბაზა
-- Database for Cars

-- ცხრილის შექმნა
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
);

-- მონაცემების შეტანა (Sample Data)
INSERT INTO cars (brand, model, year, vin_code, engine_volume, mileage_km, is_cleared, price, description, is_sold)
VALUES 
    ('Toyota', 'Camry', 2022, 'JTDBRFK30D2123456', 2.5, 15000, 1, 25000.00, 'თეთრი ღია ავტომობილი, ფერი დიდი მდგომარეობით', 0),
    ('BMW', 'X5', 2021, 'WBXYZ1234567890AB', 3.0, 25000, 1, 45000.50, 'ფხვნილი ძლევა, მოდერნული ტექნოლოგიები', 0),
    ('Mercedes-Benz', 'C-Class', 2020, 'WDDZH4GB6LF123456', 2.0, 40000, 0, 35000.00, 'ნაკრძალი, კარგი მდგომარეობა', 1),
    ('Audi', 'A4', 2023, 'WAUZZZ8K3NA123456', 1.8, 5000, 1, 38000.75, 'ახალი მსგავსი, პირველი მფლობელი', 0),
    ('Volkswagen', 'Passat', 2019, 'WVWZZZ3CZ9E123456', 1.6, 60000, 0, 18000.00, 'უმეტესად სახელმწიფოზე, ეკონომიური', 0),
    ('Honda', 'Civic', 2021, 'JHMFC7F37MU123456', 1.5, 35000, 1, 20000.00, 'საიმედო მანქანა, მომხმარებელი მოსახლეობისთვის', 0),
    ('Ford', 'Mustang', 2022, '1FA6P8TH7N5123456', 3.7, 12000, 1, 50000.99, 'სპორტული მანქანა, მძლავრი ძრავი', 0),
    ('Skoda', 'Octavia', 2020, 'TMAUZZZ8K3NA123456', 1.4, 55000, 0, 16000.50, 'ოკეანე თავის გაკრიტიკებული მდგომარეობა', 1),
    ('Hyundai', 'Elantra', 2023, 'KMHEC4A46NU123456', 1.6, 8000, 1, 19000.00, 'მცირე გარბენი, იაფი, მოსახლეობის კლასი', 0),
    ('Kia', 'Sportage', 2021, 'KNDPM3AC1L7123456', 2.0, 42000, 0, 22000.25, 'კვამფორტული SUV, ოჯახის მანქანა', 0),
    ('Mazda', 'CX-5', 2022, 'JM1BL1UJ8F0123456', 2.5, 18000, 1, 28000.75, 'დინამიური და ეკონომიური', 0),
    ('Subaru', 'Outback', 2020, 'JF1BR6SA9L5123456', 2.5, 50000, 0, 26000.00, 'AWD სისტემით, ყველა ამინდის მანქანა', 0);

-- დასრულება
SELECT COUNT(*) as total_cars FROM cars;
