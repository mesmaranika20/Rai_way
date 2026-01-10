# from datetime import datetime
# from .connection import get_connection
# import hashlib

# def hash_password(password):
#     return hashlib.sha256(password.encode()).hexdigest()

# def db_create_user(username, password):
#     conn = get_connection()
#     now = datetime.now().isoformat()
#     conn.execute(
#         "INSERT INTO users (username, password, created_at) VALUES (?, ?, ?)",
#         (username, hash_password(password), now)
#     )
#     conn.commit()
#     conn.close()

# def db_get_user(username):
#     conn = get_connection()
#     row = conn.execute(
#         "SELECT * FROM users WHERE username=?", (username,)
#     ).fetchone()
#     conn.close()
#     return dict(row) if row else None
