-- PostgreSQL example with two related tables, views, procedures, and a trigger

-- 1) Create tables
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL REFERENCES customers(customer_id) ON DELETE CASCADE,
    order_date DATE DEFAULT CURRENT_DATE,
    total_amount NUMERIC(10,2) NOT NULL,
    status VARCHAR(20) DEFAULT 'NEW'
);

-- 2) Insert sample data
INSERT INTO customers (full_name, email, phone_number, is_active)
VALUES
    ('Nika Giorgadze', 'nika@example.com', '+995591111111', TRUE),
    ('Mariam Kvaratskhelia', 'mariam@example.com', '+995592222222', FALSE);

INSERT INTO orders (customer_id, order_date, total_amount, status)
VALUES
    (1, '2026-07-01', 150.50, 'PAID'),
    (1, '2026-07-03', 89.99, 'NEW'),
    (2, '2026-07-04', 210.00, 'CANCELLED');

-- 3) Create view: all data from one table
CREATE VIEW customer_all_view AS
SELECT *
FROM customers;

-- 4) Create view: filtered data from one table
CREATE VIEW active_customers_view AS
SELECT *
FROM customers
WHERE is_active = TRUE;

-- 5) Create view: all fields from both tables
CREATE VIEW customer_orders_view AS
SELECT
    c.customer_id,
    c.full_name,
    c.email,
    c.phone_number,
    c.is_active,
    o.order_id,
    o.order_date,
    o.total_amount,
    o.status
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;

-- 6) Update view (change filter)
CREATE OR REPLACE VIEW active_customers_view AS
SELECT *
FROM customers
WHERE is_active = FALSE;

-- 7) Update view (add a column)
CREATE OR REPLACE VIEW customer_orders_view AS
SELECT
    c.customer_id,
    c.full_name,
    c.email,
    c.phone_number,
    c.is_active,
    c.created_at,
    o.order_id,
    o.order_date,
    o.total_amount,
    o.status
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;

-- 8) Drop views
DROP VIEW IF EXISTS customer_all_view;
DROP VIEW IF EXISTS active_customers_view;
DROP VIEW IF EXISTS customer_orders_view;

-- 9) Recreate views again after dropping them (optional)
CREATE VIEW customer_all_view AS
SELECT *
FROM customers;

CREATE VIEW active_customers_view AS
SELECT *
FROM customers
WHERE is_active = TRUE;

CREATE VIEW customer_orders_view AS
SELECT
    c.customer_id,
    c.full_name,
    c.email,
    c.phone_number,
    c.is_active,
    c.created_at,
    o.order_id,
    o.order_date,
    o.total_amount,
    o.status
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;

-- 10) Create procedure: delete object by id
CREATE OR REPLACE PROCEDURE delete_customer_by_id(p_customer_id INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM customers
    WHERE customer_id = p_customer_id;
END;
$$;

-- 11) Create procedure: update object by id and set provided data
CREATE OR REPLACE PROCEDURE update_customer_status_by_id(
    p_customer_id INT,
    p_is_active BOOLEAN
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE customers
    SET is_active = p_is_active,
        updated_at = CURRENT_TIMESTAMP
    WHERE customer_id = p_customer_id;
END;
$$;

-- 12) Create trigger function and trigger for updated_at
CREATE OR REPLACE FUNCTION set_updated_at()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_set_updated_at
BEFORE UPDATE ON customers
FOR EACH ROW
EXECUTE FUNCTION set_updated_at();
