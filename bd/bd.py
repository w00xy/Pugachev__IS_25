import sqlite3 as sq

# with sq.connect('saper.db') as con:
#     cur = con.cursor()
#     cur.execute("DROP TABLE IF EXISTS users")
#     cur.execute("""CREATE TABLE IF NOT EXISTS users (
#     users_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     sex INTEGER NOT NULL DEFAULT 1,
#     old INTEGER,
#     score INTEGER
#     )""")

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("INSERT INTO users VALUES (1, 'Алексей', 1, 22, 1000)")