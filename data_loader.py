import sqlite3, os
DB = os.environ.get("DB_PATH", "db.sqlite")

def init_db(conn):
    with open("schema.sql","r",encoding="utf-8") as f:
        conn.executescript(f.read())

def seed(conn):
    cur = conn.cursor()
    cur.executemany("INSERT INTO products(sku,name) VALUES(?,?)",
                    [("SKU-001","Widget A"),("SKU-002","Widget B"),("SKU-003","Widget C")])
    cur.executemany("INSERT INTO customers(name,email) VALUES(?,?)",
                    [("Acme Corp","acme@example.com"),("Globex","globex@example.com")])
    cur.executemany("INSERT INTO inventory(product_id,on_hand,reorder_point) VALUES(?,?,?)",
                    [(1,50,10),(2,5,10),(3,0,15)])
    cur.execute("INSERT INTO orders(customer_id, order_date) VALUES (1,'2025-09-01'),(2,'2025-09-05')")
    cur.executemany("INSERT INTO order_items(order_id,product_id,quantity,unit_price) VALUES (?,?,?,?)",
                    [(1,1,2,19.99),(1,2,1,29.99),(2,2,3,27.50),(2,3,1,15.00)])
    conn.commit()

if __name__ == "__main__":
    conn = sqlite3.connect(DB)
    init_db(conn); seed(conn)
    print(f"Database initialized at {DB}.")
