-- ============================================
-- ავტომანქანების მონაცემთა ბაზის ოპერაციები
-- CAR DATABASE OPERATIONS
-- ============================================

-- ============================================
-- 1. ცხრილის შექმნა და მონაცემთა ჩამატება
-- CREATE TABLE AND INSERT DATA
-- ============================================

CREATE TABLE cars (
    id INT PRIMARY KEY AUTO_INCREMENT,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    is_sold BOOLEAN DEFAULT FALSE,
    is_registered BOOLEAN DEFAULT TRUE,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ნიმუშის მონაცემი (Sample Data)
INSERT INTO cars (brand, model, year, price, is_sold, is_registered) VALUES
('Toyota', 'Corolla', 2015, 8000, FALSE, TRUE),
('BMW', 'X5', 2018, 45000, FALSE, TRUE),
('Mercedes', 'E-Class', 2012, 15000, TRUE, TRUE),
('Audi', 'A4', 2010, 12000, FALSE, FALSE),
('Honda', 'Civic', 2016, 10000, TRUE, TRUE),
('Volkswagen', 'Golf', 2014, 7500, FALSE, TRUE),
('Ford', 'Focus', 2011, 5000, FALSE, FALSE),
('Mazda', 'CX-5', 2017, 18000, FALSE, TRUE),
('Toyota', 'Camry', 2019, 22000, FALSE, TRUE),
('Tesla', 'Model 3', 2020, 35000, FALSE, TRUE);


-- ============================================
-- 2. მონაცემთა გამოტანა (DATA OUTPUT/SELECT)
-- ============================================

-- 2.1 გამოიტანეთ ყველა მონაცემის ყველა სვეტი
-- Display all columns of all data
SELECT * FROM cars;

-- 2.2 გამოიტანეთ ყველა ავტომანქანა შემდეგი სვეტებით: ბრენდი, მოდელი, წელი, ფასი
-- Display all cars with specific columns: brand, model, year, price
SELECT brand, model, year, price FROM cars;

-- 2.3 გამოიტანეთ ყველა ავტომანქანა კონკრეტული ბრენდის მიხედვით
-- Display all cars of a specific brand (example: Toyota)
SELECT * FROM cars WHERE brand = 'Toyota';

-- 2.4 გამოიტანეთ ყველა ავტომანქანა რომლის ფასი არის 2000 და 5000 შორის
-- Display all cars with price between 2000 and 5000
SELECT * FROM cars WHERE price BETWEEN 2000 AND 5000;

-- 2.5 გამოიტანეთ ყველა ავტომანქანა რომლის გამოშვების წელი არის 2010-ზე ზევით და განბაჟებულია
-- Display all cars released in 2010 or later AND are registered
SELECT * FROM cars WHERE year >= 2010 AND is_registered = TRUE;

-- ============================================
-- დამატებითი ფილტრებით (ADDITIONAL FILTERS)
-- ============================================

-- დამატებითი 1: გამოიტანეთ გაყიდული ავტომანქანები
-- Additional 1: Display sold cars
SELECT * FROM cars WHERE is_sold = TRUE;

-- დამატებითი 2: გამოიტანეთ განბაჟებული ავტომანქანები
-- Additional 2: Display registered cars
SELECT * FROM cars WHERE is_registered = TRUE;

-- დამატებითი 3: გამოიტანეთ ავტომანქანები რომელიც არ არის გაყიდული და განბაჟებულია
-- Additional 3: Display cars that are NOT sold AND registered
SELECT * FROM cars WHERE is_sold = FALSE AND is_registered = TRUE;

-- დამატებითი 4: გამოიტანეთ ავტომანქანები 2015 წლის შემდეგ დაქვეითებული სვეტებით
-- Additional 4: Display cars from 2015+ sorted by price (descending)
SELECT brand, model, year, price FROM cars WHERE year >= 2015 ORDER BY price DESC;

-- დამატებითი 5: გამოიტანეთ საშუალო ფასი ბრენდის მიხედვით
-- Additional 5: Display average price grouped by brand
SELECT brand, AVG(price) as average_price, COUNT(*) as count FROM cars GROUP BY brand;

-- დამატებითი 6: გამოიტანეთ ყველაზე ძვირი ავტომანქანა
-- Additional 6: Display most expensive car
SELECT * FROM cars ORDER BY price DESC LIMIT 1;

-- დამატებითი 7: გამოიტანეთ ყველაზე იაფი ავტომანქანა
-- Additional 7: Display cheapest car
SELECT * FROM cars ORDER BY price ASC LIMIT 1;


-- ============================================
-- 3. მონაცემთა წაშლა (DATA DELETION)
-- ============================================

-- 3.1 წაშალეთ პირველი ორი მონაცემი აიდის მიხედვით (ერთ ქვერიში)
-- Delete first two records by ID (in one query)
DELETE FROM cars WHERE id IN (1, 2);

-- 3.2 წაშალეთ ყველა ავტომანქანა რომელიც გაყიდულია
-- Delete all cars that have been sold
DELETE FROM cars WHERE is_sold = TRUE;

-- 3.3 წაშალეთ ყველა მონაცემი (მაგრამ ცხრილი რჩება)
-- Delete all data (table structure remains)
DELETE FROM cars;

-- 3.4 გაასუფთავეთ ცხრილი (უფრო სწრაფი, TRUNCATE)
-- Clear/truncate the table (faster than DELETE)
TRUNCATE TABLE cars;

-- 3.5 წაშალეთ ცხრილი სრულად
-- Drop the table completely
DROP TABLE cars;


-- ============================================
-- დამატებითი მაგალითები (ADDITIONAL EXAMPLES)
-- ============================================

-- დამატებითი წაშლა 1: წაშალეთ კონკრეტული ბრენდის ავტომანქანები
-- Additional delete 1: Delete cars of specific brand
DELETE FROM cars WHERE brand = 'Ford';

-- დამატებითი წაშლა 2: წაშალეთ 2010 წლამდე გამოშვებული ავტომანქანები
-- Additional delete 2: Delete cars released before 2010
DELETE FROM cars WHERE year < 2010;

-- დამატებითი წაშლა 3: წაშალეთ განბაჟებული კი არ არის ავტომანქანები
-- Additional delete 3: Delete unregistered cars
DELETE FROM cars WHERE is_registered = FALSE;

-- დამატებითი წაშლა 4: წაშალეთ 5000-ზე იაფი ავტომანქანები
-- Additional delete 4: Delete cars cheaper than 5000
DELETE FROM cars WHERE price < 5000;
