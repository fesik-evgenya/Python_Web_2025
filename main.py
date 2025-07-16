# Введение во Flask
# MVC - (model view controller)
# метод GET - запрашивает данные (read)
# POST - отправляет данные на сервер (submit)
# PUT - принудительно заменяет всё на сервере из контеста запроса(cхоже с методом UPDATE в sql)
# DELETE - удаляет указанные данные
# PATCH - частичное изменение данных

from flask import Flask, url_for, request
import sqlite3

# регистрируем приложение
app = Flask(__name__)
debug = False


# функция обратного вызова всегда возвращает только строку
@app.route('/')
@app.route('/index')
def index():
    return 'Привет, Flask'


@app.route('/about')
def about():
    print('Вызвана функция about')
    return 'О нас'


@app.route('/countdown')
def cd():
    lst = [str(x) for x in reversed(range(10))]
    lst.append('Полетели!!!')
    return '<br>'.join(lst)


# статический контент
# для отображения картинок, шрифтов, и прочего
# весь код фронтендовского сайта должен лежать в папке 'static'
@app.route('/image')
def show_image():
    return f'<img src="{url_for('static', filename='images/sunny_day_2.jpg')}">'

# прописываем страницу вручную (плохой вариант!!!)
@app.route('/sample-page')
def sample_page():
    return f"""
          <!DOCTYPE html>
          <html lang="ru">
          <head>
          <meta charset="UTF-8">
          <title>Хорошее настроение</title>
          </head>
          <body>
            <div>
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Earum, eligendi.</p>
            </div>
            <div>
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias eligendi illum natus quae quos? Cum cumque ea
                    illo labore mollitia nisi pariatur qui. Aperiam iste laboriosam libero, quasi veritatis voluptatem?</p>
            </div>
            <img src="{url_for('static', filename='images/sunny_day_2.jpg')}" alt="солнечный день">
          </body>
          </html>
    """

# загружаем страницу файлом html
@app.route('/sample-page-2')
def sample_page2():
    with open('temp.html', 'r', encoding='utf-8') as html:
        return html.read()

# так делать не надо!!!
x = 5
@app.route('/bad-sample')
def shoe_num():
    global x
    x += 1
    return str(x)

# <string> - по умолчанию строка
# <int:number> - целое
# <float:number> - дес. дробь
# <path:p> - может содержать '/' для указания пути
# <uuid:id> - строка-идентификатор (16-байт в HEX формате)
@app.route('/greeting/<user>')
def greeting(user):
    return f'Привет, {user}'

@app.route('/greeting/<user>/<int:id_num>')
def greeting2(user, id_num):
    return f'Привет, {user} c id={id_num}'

# тянем с базы по определённым условиям и отображаем на странице
# если id нет, то прийдёт ответ об этом пользователю
@app.route('/get-user/')
@app.route('/get-user/<int:id_num>')
def get_user(id_num=None):
    if id_num is None:
        return 'Нет номера записи'
    connection = sqlite3.connect('./db/movies.sqlite')
    cursor = connection.cursor()

    result = cursor.execute(
        f"""
        SELECT name, city
        FROM users
        WHERE trip_id = {id_num}
        """
    ).fetchone()
    name, city = result
    cursor.close()
    connection.close()
    return f'{name} из города {city}'

# работаем с формой
@app.route('/form-test', methods=['POST', 'GET'])
def form_test():
    if request.method == 'GET':
        with open('form.html', 'r', encoding='utf-8') as html:
            return html.read()
    elif request.method == 'POST':
        print(request.form)
        return 'Форма успешно отправлена'


# локальный хост - 127.0.0.1
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=debug)
