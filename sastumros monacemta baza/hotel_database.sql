-- სასტუმროს მონაცემთა ბაზა
-- Hotel Database Schema and Operations

-- ====================================
-- 1. ცხრილების წაშლა (თუ უკვე არსებობს)
-- ====================================
DROP TABLE IF EXISTS services;
DROP TABLE IF EXISTS guests;
DROP TABLE IF EXISTS rooms;
DROP TABLE IF EXISTS hotels;

-- ====================================
-- 2. ცხრილების შექმნა
-- ====================================

-- სასტუმროები ცხრილი
CREATE TABLE hotels (
    hotel_id INT PRIMARY KEY AUTO_INCREMENT,
    hotel_name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    stars INT NOT NULL CHECK (stars >= 1 AND stars <= 5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ნომრები ცხრილი
CREATE TABLE rooms (
    room_id INT PRIMARY KEY AUTO_INCREMENT,
    hotel_id INT NOT NULL,
    room_number VARCHAR(20) NOT NULL,
    floor INT NOT NULL,
    price_per_night DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (hotel_id) REFERENCES hotels(hotel_id) ON DELETE CASCADE,
    UNIQUE KEY unique_room_per_hotel (hotel_id, room_number)
);

-- სტუმრები ცხრილი
CREATE TABLE guests (
    guest_id INT PRIMARY KEY AUTO_INCREMENT,
    room_id INT NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id) ON DELETE CASCADE
);

-- სერვისები ცხრილი
CREATE TABLE services (
    service_id INT PRIMARY KEY AUTO_INCREMENT,
    room_id INT NOT NULL,
    service_name VARCHAR(100) NOT NULL,
    service_price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id) ON DELETE CASCADE
);

-- ====================================
-- 3. მონაცემების დამატება
-- ====================================

-- სასტუმროები დამატება
INSERT INTO hotels (hotel_name, city, stars) VALUES
('კაიტანი', 'თბილისი', 5),
('ფერენცი', 'ბათუმი', 4);

-- ნომრები დამატება
-- თბილისის სასტუმროს ნომრები
INSERT INTO rooms (hotel_id, room_number, floor, price_per_night) VALUES
(1, '101', 1, 150.00),
(1, '102', 1, 150.00),
(1, '201', 2, 180.00);

-- ბათუმის სასტუმროს ნომრები
INSERT INTO rooms (hotel_id, room_number, floor, price_per_night) VALUES
(2, '101', 1, 100.00),
(2, '102', 1, 100.00),
(2, '201', 2, 120.00);

-- სტუმრები დამატება
-- ნომერი 101 - თბილისი
INSERT INTO guests (room_id, first_name, last_name, phone_number) VALUES
(1, 'გიორგი', 'წერეთელი', '555-1111'),
(1, 'მარიამ', 'ღვინიოს', '555-2222');

-- ნომერი 102 - თბილისი
INSERT INTO guests (room_id, first_name, last_name, phone_number) VALUES
(2, 'დავით', 'ბექარი', '555-3333'),
(2, 'სოფო', 'ბერიძე', '555-4444');

-- ნომერი 201 - თბილისი
INSERT INTO guests (room_id, first_name, last_name, phone_number) VALUES
(3, 'ნიკა', 'გოგიბერიძე', '555-5555'),
(3, 'ამა', 'შაშკინი', '555-6666');

-- ნომერი 101 - ბათუმი
INSERT INTO guests (room_id, first_name, last_name, phone_number) VALUES
(4, 'ანა', 'ღვინიოს', '555-7777'),
(4, 'სერგო', 'გაცელია', '555-8888');

-- ნომერი 102 - ბათუმი
INSERT INTO guests (room_id, first_name, last_name, phone_number) VALUES
(5, 'თეა', 'მოსიძე', '555-9999'),
(5, 'ზაზა', 'ზოსიმ', '555-0000');

-- ნომერი 201 - ბათუმი
INSERT INTO guests (room_id, first_name, last_name, phone_number) VALUES
(6, 'თინა', 'სამღებლოვი', '555-1010'),
(6, 'რევაზი', 'ხარინი', '555-1212');

-- სერვისები დამატება
-- ნომერი 101 - თბილისი
INSERT INTO services (room_id, service_name, service_price) VALUES
(1, 'კვამლის აკრძალვა', 0.00),
(1, 'მინი ბარი', 25.00);

-- ნომერი 102 - თბილისი
INSERT INTO services (room_id, service_name, service_price) VALUES
(2, 'დილის საჭმელი', 15.00),
(2, 'ქარ აკონდიცია', 0.00);

-- ნომერი 201 - თბილისი
INSERT INTO services (room_id, service_name, service_price) VALUES
(3, 'სპა მომსახურება', 50.00),
(3, 'ჯიმი', 0.00);

-- ნომერი 101 - ბათუმი
INSERT INTO services (room_id, service_name, service_price) VALUES
(4, 'კვამლის აკრძალვა', 0.00),
(4, 'ზღვის თამაში', 30.00);

-- ნომერი 102 - ბათუმი
INSERT INTO services (room_id, service_name, service_price) VALUES
(5, 'დილის საჭმელი', 12.00),
(5, 'მინი ბარი', 20.00);

-- ნომერი 201 - ბათუმი
INSERT INTO services (room_id, service_name, service_price) VALUES
(6, 'სპა მომსახურება', 45.00),
(6, 'პარკი', 0.00);

-- ====================================
-- 4. SELECT მოთხოვნები (ძირითადი)
-- ====================================

-- 4.1: ყველა ნომერი შესაბამისი სასტუმროს სახელთან ერთად
SELECT 
    r.room_id,
    r.room_number,
    r.floor,
    r.price_per_night,
    h.hotel_name,
    h.city
FROM rooms r
JOIN hotels h ON r.hotel_id = h.hotel_id
ORDER BY h.hotel_name, r.room_number;

-- 4.2: ყველა სტუმარი მისი ნომრის ნომრითა და სასტუმროს სახელით
SELECT 
    g.guest_id,
    CONCAT(g.first_name, ' ', g.last_name) AS guest_name,
    g.phone_number,
    r.room_number,
    h.hotel_name,
    h.city
FROM guests g
JOIN rooms r ON g.room_id = r.room_id
JOIN hotels h ON r.hotel_id = h.hotel_id
ORDER BY h.hotel_name, r.room_number;

-- 4.3: კონკრეტული სასტუმროს ყველა სტუმარი (კაიტანი)
SELECT 
    CONCAT(g.first_name, ' ', g.last_name) AS guest_name,
    g.phone_number,
    r.room_number,
    h.hotel_name
FROM guests g
JOIN rooms r ON g.room_id = r.room_id
JOIN hotels h ON r.hotel_id = h.hotel_id
WHERE h.hotel_name = 'კაიტანი'
ORDER BY r.room_number;

-- 4.4: თითო სასტუმროში არსებული ნომრების რაოდენობა
SELECT 
    h.hotel_id,
    h.hotel_name,
    h.city,
    COUNT(r.room_id) AS room_count
FROM hotels h
LEFT JOIN rooms r ON h.hotel_id = r.hotel_id
GROUP BY h.hotel_id, h.hotel_name, h.city
ORDER BY h.hotel_name;

-- 4.5: იმ ნომრებს, რომელთათვისაც სერვისი ჯერ არ არის შეკვეთილი
SELECT 
    r.room_id,
    r.room_number,
    r.floor,
    h.hotel_name,
    r.price_per_night
FROM rooms r
JOIN hotels h ON r.hotel_id = h.hotel_id
LEFT JOIN services s ON r.room_id = s.room_id
WHERE s.service_id IS NULL
ORDER BY h.hotel_name, r.room_number;

-- ====================================
-- 5. დამატებითი ინფორმაციული მოთხოვნები
-- ====================================

-- სტუმრების რაოდენობა თითო ნომერში
SELECT 
    r.room_id,
    r.room_number,
    h.hotel_name,
    COUNT(g.guest_id) AS guest_count
FROM rooms r
JOIN hotels h ON r.hotel_id = h.hotel_id
LEFT JOIN guests g ON r.room_id = g.room_id
GROUP BY r.room_id, r.room_number, h.hotel_name
ORDER BY h.hotel_name, r.room_number;

-- სერვისების რაოდენობა და მათი ჯამური ღირებულება ნომერზე
SELECT 
    r.room_id,
    r.room_number,
    h.hotel_name,
    COUNT(s.service_id) AS service_count,
    SUM(s.service_price) AS total_service_price
FROM rooms r
JOIN hotels h ON r.hotel_id = h.hotel_id
LEFT JOIN services s ON r.room_id = s.room_id
GROUP BY r.room_id, r.room_number, h.hotel_name
ORDER BY h.hotel_name, r.room_number;

-- ====================================
-- 6. DELETE, UPDATE, და სხვა ოპერაციები
-- ====================================

-- 6.1: წაშალეთ ერთი ნომერი (მაგ. ნომერი 102 თბილისიდან - room_id = 2)
-- ეს ოპერაცია იშლის ღირებულებაში დაკავშირებულ სტუმრებსა და სერვისებს
-- DELETE FROM rooms WHERE room_id = 2;

-- 6.2: შეცვალეთ კონკრეტული ნომრის ღირებულება
-- UPDATE rooms SET price_per_night = 200.00 WHERE room_id = 1;

-- 6.3: ერთი სტუმარი გადააწერეთ სხვა ნომერზე
-- UPDATE guests SET room_id = 3 WHERE guest_id = 1;

-- ====================================
-- 7. მოთხოვნები ოპერაციების შემდეგ
-- ====================================

-- დაამოწმეთ მოთხოვნა ოპერაციების შემდეგ:
-- SELECT * FROM guests;
-- SELECT * FROM rooms;
-- SELECT * FROM services;
-- SELECT * FROM hotels;
