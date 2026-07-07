DROP TABLE IF EXISTS products;

CREATE TABLE products (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  quantity INT NOT NULL,
  status VARCHAR(20)
);

DELIMITER $$

CREATE TRIGGER trg_products_bi
BEFORE INSERT ON products
FOR EACH ROW
BEGIN
  IF NEW.quantity = 0 THEN
    SET NEW.status = 'out of stock';
  ELSEIF NEW.quantity BETWEEN 1 AND 10 THEN
    SET NEW.status = 'low stock';
  ELSE
    SET NEW.status = 'in stock';
  END IF;
END$$

CREATE TRIGGER trg_products_bu
BEFORE UPDATE ON products
FOR EACH ROW
BEGIN
  IF NEW.quantity = 0 THEN
    SET NEW.status = 'out of stock';
  ELSEIF NEW.quantity BETWEEN 1 AND 10 THEN
    SET NEW.status = 'low stock';
  ELSE
    SET NEW.status = 'in stock';
  END IF;
END$$

CREATE PROCEDURE decrease_stock(IN p_id INT, IN p_quantity INT)
BEGIN
  UPDATE products
  SET quantity = quantity - p_quantity
  WHERE id = p_id;
END$$

DELIMITER ;

-- Sample data (status is not provided manually)
INSERT INTO products (name, price, quantity) VALUES
  ('Product 1', 150.00, 5),
  ('Product 2', 250.00, 0),
  ('Product 3', 320.00, 12),
  ('Product 4', 90.00, 8),
  ('Product 5', 500.00, 20);

CALL decrease_stock(1, 2);

SELECT id, name, price, quantity, status FROM products ORDER BY id;
