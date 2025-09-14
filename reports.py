import sqlite3, os
DB = os.environ.get("DB_PATH","db.sqlite")

QUERIES = {
 "monthly_sales": """
  SELECT strftime('%Y-%m', o.order_date) AS month,
         ROUND(SUM(oi.quantity*oi.unit_price),2) AS revenue
  FROM orders o JOIN order_items oi ON oi.order_id=o.order_id
  GROUP BY month ORDER BY month;""",
 "stock_shortages": """
  SELECT p.sku,p.name,i.on_hand,i.reorder_point
  FROM inventory i JOIN products p ON p.product_id=i.product_id
  WHERE i.on_hand < i.reorder_point ORDER BY i.on_hand ASC;"""
}

def run_query(name):
    conn = sqlite3.connect(DB)
    cur = conn.cursor(); cur.execute(QUERIES[name])
    return [c[0] for c in cur.description], cur.fetchall()

if __name__ == "__main__":
    for q in QUERIES:
        cols, rows = run_query(q)
        print("===", q, "==="); print(cols); [print(r) for r in rows]
