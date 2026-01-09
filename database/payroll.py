from datetime import datetime
from .connection import get_connection

def db_get_all():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM payroll").fetchall()
    conn.close()
    return [dict(r) for r in rows]

def db_create(data):
    conn = get_connection()
    now = datetime.now().isoformat()
    conn.execute(
        "INSERT INTO payroll (staff_id, salary, month, created_at) VALUES (?, ?, ?, ?)",
        (data["staff_id"], data["salary"], data["month"], now)
    )
    conn.commit()
    conn.close()
