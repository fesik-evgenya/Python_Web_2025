# Введение во Flask
# MVC - (model view controller)
# метод GET - запрашивает данные (read)
# POST - отправляет данные на сервер (submit)
# PUT - принудительно заменяет всё на сервере из контеста запроса(cхоже с методом UPDATE в sql)
# DELETE - удаляет указанные данные
# PATCH - частичное изменение данных
# шаблонизатор JINJA - переменные, условия, циклы и т.д.
# ORM - Object Relational Mapping

from flask import Flask, url_for, request, render_template
from openpyxl.styles.builtins import title
from werkzeug.utils import secure_filename
import os.path
import sqlite3
from forms.loginform import LoginForm
from data import db_session

# регистрируем приложение
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload/'
app.config['SECRET_KEY'] = 'just_secret_key'
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'zip', 'jpg', 'png']
debug = False


# проверка загруженного файла на нужное расширение
def allowed_file(filename):
    return ('.' in filename and
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS)


# функция обратного вызова всегда возвращает только строку
@app.route('/')
@app.route('/index')
def index():
    params = {}
    params['user'] = 'слушатель'
    params['title'] = 'приветствие'
    params['weather'] = 'Сегодня хорошая погода'
    return render_template('index.html', **params)


@app.route('/about')
def about():
    params = {}
    params['price'] = 'price'
    return render_template('about.html', **params)


@app.route('/contacts')
def contacts():
    params = {}
    params['phone'] = '+7 (991) 366-60-60'
    params['email'] = 'my-longhair@mail.ru'
    params['address'] = 'г. Ростов-на-Дону, Нахичевань, 30-я Линия д.15'
    params['vk_group'] = 'https://vk.com/narashchivanie_rostov'
    return render_template('contacts.html', **params)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return 'Форма отправлена'
    return render_template('login.html', title='Авторизация', form=form)


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


# как принять файл с сайта и положить в нужное место на сервере (предварительно проверить)
@app.route('/upload', methods=['POST', 'GET'])
def file_upload():
    if request.method == 'GET':
        with open('upload.html', 'r', encoding='utf-8') as html:
            return html.read()
    elif request.method == 'POST':
        if 'file' not in request.files:
            return 'Файл не был выбран!!!'

        file = request.files['file']

        if file.filename == '':
            return 'Файл без имени'

        if file and allowed_file(file.filename):
            new_name = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_name))
            return f'Файл {new_name} загружен успешно'
    return 'Ошибка загрузки'


@app.route('/numbers/')
@app.route('/numbers/<int:num>')
def odd_even(num=None):
    if num is None:
        return render_template('numbers.html', title="Нет числа", number='')
    return render_template('numbers.html', title='Чёт-нечёт', number=num)


@app.route('/deals')
def print_list():
    deal = ['Помыть посуду', 'Выгулять собаку', 'Снять показание счётчика', 'Сходить в магазин']
    return render_template('printlist.html', deals=deal)


@app.route('/queue')
def queue():
    # loop.index - номер итерации начиная с 1
    # loop.index0 - номер итерации начиная с 0
    # loop.first - True, если первая итерация
    # loop.last - True, если последняя итерация
    return render_template('vars.html', title='Стоим в очереди')


# локальный хост - 127.0.0.1
if __name__ == '__main__':
    db_session.global_init('db/news.sqlite')
    app.run(host='localhost', port=5000, debug=debug)
