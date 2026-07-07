import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("products.db")

SQL = """
DROP TABLE IF EXISTS products;

CREATE TABLE products (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  price REAL NOT NULL,
  quantity INTEGER NOT NULL,
  status TEXT
);

CREATE TRIGGER trg_products_ai
AFTER INSERT ON products
FOR EACH ROW
BEGIN
  UPDATE products
  SET status = CASE
    WHEN NEW.quantity = 0 THEN 'out of stock'
    WHEN NEW.quantity BETWEEN 1 AND 10 THEN 'low stock'
    ELSE 'in stock'
  END
  WHERE id = NEW.id;
END;

CREATE TRIGGER trg_products_au
AFTER UPDATE OF quantity ON products
FOR EACH ROW
BEGIN
  UPDATE products
  SET status = CASE
    WHEN NEW.quantity = 0 THEN 'out of stock'
    WHEN NEW.quantity BETWEEN 1 AND 10 THEN 'low stock'
    ELSE 'in stock'
  END
  WHERE id = NEW.id;
END;
"""


def create_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(SQL)


def decrease_stock(conn: sqlite3.Connection, product_id: int, quantity: int) -> None:
    conn.execute(
        "UPDATE products SET quantity = quantity - ? WHERE id = ?",
        (quantity, product_id),
    )
    conn.commit()


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    create_schema(conn)

    products = [
        ("Product 1", 150.0, 5),
        ("Product 2", 250.0, 0),
        ("Product 3", 320.0, 12),
        ("Product 4", 90.0, 8),
        ("Product 5", 500.0, 20),
    ]

    conn.executemany(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        products,
    )
    conn.commit()

    decrease_stock(conn, 1, 2)

    rows = conn.execute(
        "SELECT id, name, price, quantity, status FROM products ORDER BY id"
    ).fetchall()
    print("id | name | price | quantity | status")
    for row in rows:
        print(row)

    conn.close()


if __name__ == "__main__":
    main()
