# Базы данных (чтение)
"""
1. Импорт библиотеки sqlite3
2. Подключаемся к БД
3. Назначить "курсор"
4. Работаем с БД ( запросы и ответы)
5. Отключаемся от БД
"""
import sqlite3

# подключаемся
connection = sqlite3.connect('./db/movies.sqlite')

# Курсор
cursor = connection.cursor()

# запрос ( с помощью курсора)
result = cursor.execute(
    """
    SELECT title, year
    FROM films
    WHERE year = 2010
    """
)

# fetchall() - всё; fetchone() - один, первый; fetchmany(5) - первые 5 шт
array = result.fetchall()
for title, year in array:
    print(f'Фильм "{title}" вышел в {year} году.')