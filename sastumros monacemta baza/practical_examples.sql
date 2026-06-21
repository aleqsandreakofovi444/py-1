-- ====================================
-- პრაქტიკული გამოყენების მაგალითები
-- Hotel Database - Practical Examples
-- ====================================

-- ====================================
-- ᲜᲐᲬᲘᲚᲘ 1: ბაზაზე და მონაცემებზე დაკვირვება
-- ====================================

-- 1.1 ყველა სასტუმროს ნახვა
SELECT * FROM hotels;

-- 1.2 ყველა ნომრის ნახვა
SELECT * FROM rooms;

-- 1.3 ყველა სტუმრის ნახვა
SELECT * FROM guests;

-- 1.4 ყველა სერვისის ნახვა
SELECT * FROM services;

-- ====================================
-- ᲜᲐᲬᲘᲚᲘ 2: JOIN მოთხოვნები
-- ====================================

-- 2.1 ყველა ნომერი თავიანთი სასტუმროს სახელთან
SELECT 
    r.room_id,
    CONCAT('Room ', r.room_number) as room_info,
    CONCAT('Floor ', r.floor) as floor_info,
    r.price_per_night,
    h.hotel_name,
    h.city
FROM rooms r
INNER JOIN hotels h ON r.hotel_id = h.hotel_id
ORDER BY h.hotel_name, r.room_number;

-- 2.2 სტუმრების სრული ინფორმაცია თავიანთი ნომრებით
SELECT 
    CONCAT(g.first_name, ' ', g.last_name) as full_name,
    g.phone_number,
    r.room_number,
    r.floor,
    h.hotel_name,
    h.city,
    r.price_per_night
FROM guests g
INNER JOIN rooms r ON g.room_id = r.room_id
INNER JOIN hotels h ON r.hotel_id = h.hotel_id
ORDER BY h.hotel_name, r.room_number, g.last_name;

-- 2.3 თითოეული ნომრის სერვისები
SELECT 
    h.hotel_name,
    r.room_number,
    s.service_name,
    s.service_price
FROM services s
INNER JOIN rooms r ON s.room_id = r.room_id
INNER JOIN hotels h ON r.hotel_id = h.hotel_id
ORDER BY h.hotel_name, r.room_number, s.service_name;

-- ====================================
-- ᲜᲐᲬᲘᲚᲘ 3: ანალიტიკური მოთხოვნები
-- ====================================

-- 3.1 თითო სასტუმროში რამდენი ნომერია
SELECT 
    h.hotel_name,
    h.city,
    h.stars,
    COUNT(r.room_id) as room_count
FROM hotels h
LEFT JOIN rooms r ON h.hotel_id = r.hotel_id
GROUP BY h.hotel_id, h.hotel_name, h.city, h.stars;

-- 3.2 თითო ნომერში რამდენი სტუმარია
SELECT 
    h.hotel_name,
    r.room_number,
    r.price_per_night,
    COUNT(g.guest_id) as guest_count
FROM rooms r
LEFT JOIN guests g ON r.room_id = g.room_id
LEFT JOIN hotels h ON r.hotel_id = h.hotel_id
GROUP BY r.room_id, h.hotel_name, r.room_number, r.price_per_night
ORDER BY h.hotel_name, r.room_number;

-- 3.3 თითო ნომერზე რამდენი სერვისია და მათი ჯამი
SELECT 
    h.hotel_name,
    r.room_number,
    r.price_per_night,
    COUNT(s.service_id) as service_count,
    COALESCE(SUM(s.service_price), 0) as total_service_price
FROM rooms r
LEFT JOIN services s ON r.room_id = s.room_id
LEFT JOIN hotels h ON r.hotel_id = h.hotel_id
GROUP BY r.room_id, h.hotel_name, r.room_number, r.price_per_night
ORDER BY h.hotel_name, r.room_number;

-- 3.4 საშუალო ღირებულება სასტუმროს მიხედვით
SELECT 
    h.hotel_name,
    h.city,
    AVG(r.price_per_night) as avg_price,
    MIN(r.price_per_night) as min_price,
    MAX(r.price_per_night) as max_price
FROM rooms r
LEFT JOIN hotels h ON r.hotel_id = h.hotel_id
GROUP BY h.hotel_id, h.hotel_name, h.city;

-- ====================================
-- ᲜᲐᲬᲘᲚᲘ 4: ფილტრირებული მოთხოვნები
-- ====================================

-- 4.1 კონკრეტული სასტუმროს ყველა სტუმარი (კაიტანი)
SELECT 
    CONCAT(g.first_name, ' ', g.last_name) as full_name,
    g.phone_number,
    r.room_number,
    r.floor
FROM guests g
INNER JOIN rooms r ON g.room_id = r.room_id
INNER JOIN hotels h ON r.hotel_id = h.hotel_id
WHERE h.hotel_name = 'კაიტანი'
ORDER BY r.room_number, g.last_name;

-- 4.2 კონკრეტული სასტუმროს ყველა ნომერი
SELECT 
    r.room_id,
    r.room_number,
    r.floor,
    r.price_per_night,
    COUNT(DISTINCT g.guest_id) as guest_count
FROM rooms r
LEFT JOIN guests g ON r.room_id = g.room_id
WHERE r.hotel_id = (SELECT hotel_id FROM hotels WHERE hotel_name = 'კაიტანი')
GROUP BY r.room_id, r.room_number, r.floor, r.price_per_night
ORDER BY r.room_number;

-- 4.3 ის ნომრები რომელთებსაც ჯერ სერვისი არ აქვთ
SELECT 
    h.hotel_name,
    r.room_id,
    r.room_number,
    r.floor,
    r.price_per_night
FROM rooms r
LEFT JOIN hotels h ON r.hotel_id = h.hotel_id
WHERE NOT EXISTS (
    SELECT 1 FROM services s WHERE s.room_id = r.room_id
)
ORDER BY h.hotel_name, r.room_number;

-- 4.4 ღამის ღირებულების შედარება
SELECT 
    h.hotel_name,
    r.room_number,
    r.price_per_night,
    CASE 
        WHEN r.price_per_night < 120 THEN 'Cheap'
        WHEN r.price_per_night BETWEEN 120 AND 160 THEN 'Medium'
        ELSE 'Expensive'
    END as price_category
FROM rooms r
LEFT JOIN hotels h ON r.hotel_id = h.hotel_id
ORDER BY r.price_per_night DESC;

-- ====================================
-- ᲜᲐᲬᲘᲚᲘ 5: DELETE ოპერაციების მაგალითები
-- ====================================

-- 5.1 ნომერი 102 თბილისიდან წაშლა (room_id = 2)
-- BEFORE: ეს ნომერი აქვს 2 სტუმარი და 2 სერვისი
-- AFTER: ყველა წაიშლება ავტომატურად CASCADE DELETE-ს გამო

-- მოთხოვნა წაშლამდე: დააკვირდით მონაცემებს
SELECT 'Before DELETE' as status;
SELECT COUNT(*) as room_count FROM rooms;
SELECT COUNT(*) as guest_count FROM guests WHERE room_id = 2;
SELECT COUNT(*) as service_count FROM services WHERE room_id = 2;

-- წაშლა (კომენტარი ამოხსენით შესასრულებლად)
-- DELETE FROM rooms WHERE room_id = 2;

-- მოთხოვნა წაშლის შემდეგ: დააკვირდით კასკადური ეფექტს
-- SELECT 'After DELETE' as status;
-- SELECT COUNT(*) as room_count FROM rooms;
-- SELECT COUNT(*) as guest_count FROM guests;
-- SELECT COUNT(*) as service_count FROM services;

-- ====================================
-- ᲜᲐᲬᲘᲚᲘ 6: UPDATE ოპერაციების მაგალითები
-- ====================================

-- 6.1 ნომერი 101-ის ღირებულება შეცვალეთ
-- მოთხოვნა განახლებამდე:
SELECT room_number, price_per_night FROM rooms WHERE room_id = 1;

-- განახლება (კომენტარი ამოხსენით შესასრულებლად)
-- UPDATE rooms SET price_per_night = 200.00 WHERE room_id = 1;

-- მოთხოვნა განახლების შემდეგ:
-- SELECT room_number, price_per_night FROM rooms WHERE room_id = 1;

-- 6.2 თითოეული ნომრის ღირებულება 10%-ით გაზარდეთ
-- UPDATE rooms SET price_per_night = price_per_night * 1.10;

-- 6.3 კონკრეტული ოთახის ღირებულება განახლება უფრო რთული პირობით
-- UPDATE rooms 
-- SET price_per_night = price_per_night * 1.05 
-- WHERE floor = 2;

-- ====================================
-- ᲜᲐᲬᲘᲚᲘ 7: სტუმარის გადაწერა ოპერაციები
-- ====================================

-- 7.1 სტუმარი გადააწერეთ სხვა ნომერზე
-- მოთხოვნა ოპერაციამდე:
SELECT g.guest_id, CONCAT(g.first_name, ' ', g.last_name) as name, g.room_id 
FROM guests WHERE guest_id = 1;

-- ოპერაცია (კომენტარი ამოხსენით შესასრულებლად)
-- UPDATE guests SET room_id = 3 WHERE guest_id = 1;

-- მოთხოვნა ოპერაციის შემდეგ:
-- SELECT g.guest_id, CONCAT(g.first_name, ' ', g.last_name) as name, 
--        CONCAT('Room ', r.room_number) as room
-- FROM guests g
-- JOIN rooms r ON g.room_id = r.room_id
-- WHERE guest_id = 1;

-- ====================================
-- ᲜᲐᲬᲘᲚᲘ 8: რეპორტები
-- ====================================

-- 8.1 სრული რეპორტი ყველა ინფორმაციით
SELECT 
    h.hotel_name,
    h.stars,
    r.room_number,
    r.floor,
    r.price_per_night,
    CONCAT(g.first_name, ' ', g.last_name) as guest_name,
    g.phone_number,
    s.service_name,
    s.service_price
FROM hotels h
LEFT JOIN rooms r ON h.hotel_id = r.hotel_id
LEFT JOIN guests g ON r.room_id = g.room_id
LEFT JOIN services s ON r.room_id = s.room_id
ORDER BY h.hotel_name, r.room_number, g.last_name, s.service_name;

-- 8.2 სტატისტიკა სასტუმროს მიხედვით
SELECT 
    h.hotel_name,
    h.city,
    h.stars,
    COUNT(DISTINCT r.room_id) as room_count,
    COUNT(DISTINCT g.guest_id) as guest_count,
    COUNT(DISTINCT s.service_id) as service_count,
    AVG(r.price_per_night) as avg_room_price
FROM hotels h
LEFT JOIN rooms r ON h.hotel_id = r.hotel_id
LEFT JOIN guests g ON r.room_id = g.room_id
LEFT JOIN services s ON r.room_id = s.room_id
GROUP BY h.hotel_id, h.hotel_name, h.city, h.stars;

-- 8.3 უმაღლესი დასახელებული სერვისები
SELECT 
    s.service_name,
    COUNT(*) as usage_count,
    AVG(s.service_price) as avg_price,
    MAX(s.service_price) as max_price
FROM services s
GROUP BY s.service_name
ORDER BY usage_count DESC, avg_price DESC;

-- ====================================
-- ᲜᲐᲬᲘᲚᲘ 9: სანამ-გან და შემდეგ ზომებიანი მოთხოვნები
-- ====================================

-- 9.1 გამოთვალეთ სტუმრებისა და სერვისების რაოდენობა მოთხოვნის შემდეგ
SELECT 
    'Data Summary' as report_title,
    (SELECT COUNT(*) FROM hotels) as total_hotels,
    (SELECT COUNT(*) FROM rooms) as total_rooms,
    (SELECT COUNT(*) FROM guests) as total_guests,
    (SELECT COUNT(*) FROM services) as total_services;

-- 9.2 თითოეული ნომრის სახელმწიფო
SELECT 
    r.room_id,
    CONCAT('Room ', r.room_number) as room,
    (SELECT COUNT(*) FROM guests WHERE room_id = r.room_id) as guest_count,
    (SELECT COUNT(*) FROM services WHERE room_id = r.room_id) as service_count
FROM rooms r
ORDER BY r.room_id;

-- ====================================
-- ᲜᲐᲬᲘᲚᲘ 10: რთული მოთხოვნები
-- ====================================

-- 10.1 სასტუმროები ოთხი ან მეტი ვარსკვალით რომელთებსაც სამიდან მეტი ნომერი აქვთ
SELECT 
    h.hotel_name,
    h.stars,
    COUNT(r.room_id) as room_count,
    AVG(r.price_per_night) as avg_price
FROM hotels h
LEFT JOIN rooms r ON h.hotel_id = r.hotel_id
WHERE h.stars >= 4
GROUP BY h.hotel_id, h.hotel_name, h.stars
HAVING COUNT(r.room_id) >= 3;

-- 10.2 სტუმრები რომელთებიც აკვირდებენ ნომრებს ნულოვანი დამატებითი სერვისით
SELECT 
    CONCAT(g.first_name, ' ', g.last_name) as guest_name,
    r.room_number,
    COUNT(s.service_id) as service_count
FROM guests g
JOIN rooms r ON g.room_id = r.room_id
LEFT JOIN services s ON r.room_id = s.room_id
GROUP BY g.guest_id, g.first_name, g.last_name, r.room_number
HAVING COUNT(s.service_id) = 0;

-- ====================================
-- ᲨᲔᲜᲘᲨᲕᲜᲐ
-- ====================================
-- DELETE და UPDATE მოთხოვნები კომენტარშია კომენტარი ამოხსენით
-- SELECT მოთხოვნებიდან დაიწყეთ მონაცემების გაგებასთან
-- თითოეული ოპერაციის შემდეგ გაიმეორეთ SELECT მოთხოვნები შედეგის დასაკვირვებლად
