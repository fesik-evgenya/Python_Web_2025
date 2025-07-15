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

# добавили значения в таблицу
INSERT INTO 
users(name, age)
VALUES('Tom', 20),
('Tim', 45)

# изменение возраста записи
UPDATE users
SET age=22
WHERE ID=2