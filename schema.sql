PRAGMA foreign_keys = ON;

CREATE TABLE products(
  product_id INTEGER PRIMARY KEY,
  sku TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL
);
CREATE TABLE customers(
  customer_id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE
);
CREATE TABLE orders(
  order_id INTEGER PRIMARY KEY,
  customer_id INTEGER NOT NULL,
  order_date DATE NOT NULL,
  FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);
CREATE TABLE order_items(
  order_item_id INTEGER PRIMARY KEY,
  order_id INTEGER NOT NULL,
  product_id INTEGER NOT NULL,
  quantity INTEGER NOT NULL CHECK(quantity>0),
  unit_price REAL NOT NULL CHECK(unit_price>=0),
  FOREIGN KEY(order_id) REFERENCES orders(order_id),
  FOREIGN KEY(product_id) REFERENCES products(product_id)
);
CREATE TABLE inventory(
  product_id INTEGER PRIMARY KEY,
  on_hand INTEGER NOT NULL DEFAULT 0 CHECK(on_hand>=0),
  reorder_point INTEGER NOT NULL DEFAULT 10 CHECK(reorder_point>=0),
  FOREIGN KEY(product_id) REFERENCES products(product_id)
);
