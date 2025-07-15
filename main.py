# Базы данных (запись)
import sqlite3
import csv

# запрос (помощью курсора)
# читаем файл CSV
with open('people.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader) # пропустить заголовок

    # подключаемся
    connection = sqlite3.connect('./db/movies.sqlite')
    # курсор
    cursor = connection.cursor()
    # запрос (помощью курсора)

    for name, age in reader:
        result = cursor.execute(
            """
            INSERT INTO 
            users ('name', age)
            VALUES (?, ?)
            """, (name, int(age))
        )
    # подтверждение
    connection.commit()
    # закрываем подключение
    connection.close()