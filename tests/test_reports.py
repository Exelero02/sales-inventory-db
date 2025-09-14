import os, importlib.util
from pathlib import Path

def mod(path):
    spec = importlib.util.spec_from_file_location("reports", path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def setup_db(tmp_path):
    os.environ["DB_PATH"] = str(tmp_path/"db.sqlite")
    os.system(f"python {Path(__file__).parent.parent/'data_loader.py'} > /dev/null 2>&1")

def test_monthly_sales(tmp_path):
    setup_db(tmp_path); reports = mod(Path(__file__).parent.parent/'reports.py')
    cols, rows = reports.run_query("monthly_sales")
    assert cols == ["month","revenue"] and len(rows) >= 1 and all(r[1] >= 0 for r in rows)

def test_stock_shortages(tmp_path):
    setup_db(tmp_path); reports = mod(Path(__file__).parent.parent/'reports.py')
    _, rows = reports.run_query("stock_shortages")
    skus = [r[0] for r in rows]
    assert "SKU-002" in skus and "SKU-003" in skus
