# базы данных
# Базовый синтаксис

SELECT перечень_полей (*)
FROM имя_таблицы
WHERE условие
ORDER BY по какому полю

# пример составного запроса
SELECT title
FROM films
WHERE genre = (
SELECT id FROM genres
WHERE title = 'фантастика')

# выборка по перечню значений
SELECT title, duration
FROM films
WHERE duration in (45, 60, 90)
ORDER BY duration DESC