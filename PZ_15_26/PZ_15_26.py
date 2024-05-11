import sqlite3

connection = sqlite3.connect('pz15.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY,
        clientFullName TEXT NOT NULL,
        masterFullName TEXT NOT NULL,
        type TEXT NOT NULL,
        material TEXT NOT NULL,
        price INTEGER NOT NULL
    )
''')

connection.commit()
connection.close()



