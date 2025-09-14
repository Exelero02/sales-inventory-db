# Sales & Inventory Database Management

This project demonstrates the design and use of a **relational database** for managing sales, inventory, and customer data.  
It includes **SQL reporting queries**, **Python automation scripts**, and **automated tests** to ensure data consistency.

## Features
- **Relational schema** with products, customers, orders, order items, and inventory.
- **SQL queries** for reporting:
  - Monthly sales trends
  - Stock shortages vs. reorder points
- **Python scripts** for:
  - Initializing and seeding the database
  - Automating report execution
- **Testing** with `pytest` to validate:
  - Monthly sales query returns correct values
  - Stock shortage query flags the right products

## Tech Stack
- **SQL** (SQLite, standard SQL syntax)
- **Python** (3.9+, `sqlite3`)
- **Testing**: `pytest`

## Quickstart
```bash
# 1. Navigate to project folder
cd 01_sales_inventory_db

# 2. Create and seed database
python data_loader.py

# 3. Run reports
python reports.py

# 4. (Optional) Run tests
pytest -q
```
