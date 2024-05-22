# Приложение ЮВЕЛИРНАЯ МАСТЕРСКАЯ для некоторой организации. БД
# должна содержать таблицу Изделие со следующей структурой записи: ФИО клиента,
# ФИО мастера, вид изделия, материал, стоимость работ.

import sqlite3

connection = sqlite3.connect('pz15.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Product (
        id INTEGER PRIMARY KEY,
        clientFullName TEXT NOT NULL,
        masterFullName TEXT NOT NULL,
        type TEXT NOT NULL,
        material TEXT NOT NULL,
        price INTEGER NOT NULL
    )
''')

people = [
    (1, 'Иван Иванович Иванов', 'Петр Петрович Петров', 'Кольцо', 'Золото', 15000),
    (2, 'Мария Васильевна Кузнецова', 'Анна Сергеевна Сидорова', 'Браслет', 'Серебро', 10000),
    (3, 'Сергей Владимирович Васильев', 'Дмитрий Алексеевич Иванов', 'Серьги', 'Платина', 20000),
    (4, 'Наталья Петровна Петрова', 'Елена Владимировна Васильева', 'Колье', 'Бриллиант', 25000),
    (5, 'Александр Сергеевич Павлов', 'Игорь Геннадьевич Сергеев', 'Запонки', 'Серебро', 7000),
    (6, 'Оксана Александровна Федорова', 'Екатерина Владимировна Петрова', 'Подвеска', 'Золото', 12000),
    (7, 'Михаил Борисович Козлов', 'Алексей Дмитриевич Иванов', 'Цепочка', 'Платина', 18000),
    (8, 'Виктория Викторовна Смирнова', 'Юлия Александровна Сидорова', 'Кольцо', 'Серебро', 8000),
    (9, 'Владимир Сергеевич Соколов', 'Александр Петрович Петров', 'Браслет', 'Золото', 16000),
    (10, 'Ирина Андреевна Волкова', 'Светлана Ивановна Иванова', 'Серьги', 'Бриллиант', 22000)
]

cursor.executemany('''
 INSERT INTO Product (id, clientFullName, masterFullName, type, material, price)
 VALUES (?, ?, ?, ?, ?, ?)
''', people)

# Запросы
cursor.execute('SELECT * FROM Product')
print("Все позиции в таблице:")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT * FROM Product WHERE clientFullName = 'Иван Иванович Иванов'")
print("\nКлиент(ы) которых зовут Иван Иванович Иванов:")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT * FROM Product WHERE type = 'Кольцо' AND Product.price < 10000")
print("\nВсе колица дешевле 10000:")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT * FROM Product WHERE material = 'Золото'")
print("\nВсе изделия из материала Золото:")
for row in cursor.fetchall():
    print(row)

# update
cursor.execute("UPDATE Product SET price = 22222 WHERE material = 'Золото'")
cursor.execute("UPDATE Product SET price = 14000 WHERE type = 'Колье'")
cursor.execute("UPDATE Product SET masterFullName = 'Карим Эль-Кадри Рафикович' WHERE type = 'Цепочка'")
connection.commit()

cursor.execute("DELETE FROM Product WHERE price = 7000")
cursor.execute("DELETE FROM Product WHERE clientFullName = 'Петр Петрович Петров'")
cursor.execute("DELETE FROM Product WHERE type = 'Браслет'")

cursor.execute('SELECT * FROM Product')
print("\nВсе позиции в таблице после удаления:")
for row in cursor.fetchall():
    print(row)
connection.close()

# connection.commit()
connection.close()



