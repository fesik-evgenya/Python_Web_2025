# Введение во Flask
# MVC - (model view controller)
# метод GET - запрашивает данные (read)
# POST - отправляет данные на сервер (submit)
# PUT - принудительно заменяет всё на сервере из контеста запроса(cхоже с методом UPDATE в sql)
# DELETE - удаляет указанные данные
# PATCH - частичное изменение данных
# шаблонизатор JINJA - переменные, условия, циклы и т.д.
# ORM - Object Relational Mapping

from flask import Flask, url_for, request, render_template, redirect
from flask_login import login_manager, LoginManager, login_user, logout_user
from pyexpat.errors import messages
from werkzeug.utils import secure_filename
import os.path
import sqlite3
from forms.loginform import LoginForm
from data import db_session
from sqlite3 import Error
from data.users import User
from data.news import News
from forms.user import Register

# регистрируем приложение
app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

app.config['UPLOAD_FOLDER'] = 'upload/'
app.config['SECRET_KEY'] = 'just_secret_key'
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'zip', 'jpg', 'png']
debug = False


# проверка загруженного файла на нужное расширение
def allowed_file(filename):
    return ('.' in filename and
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


# обработка 404 (обязательно делаем!!!)
@app.errorhandler(404)
def not_found(y):
    return render_template('404.html', title="Не найдено")

# функция обратного вызова всегда возвращает только строку
@app.route('/')
@app.route('/index')
def index():
    params = dict()
    params['user'] = 'слушатель'
    params['title'] = 'приветствие'
    params['weather'] = 'Сегодня хорошая погода'
    return render_template('index.html', **params)

# добавляем иконку в превью при поисковой выдаче (размер кратен 16!!!)

@app.route('/about')
def about():
    params = dict()
    params['price'] = 'price'
    return render_template('about.html', **params)


@app.route('/contacts')
def contacts():
    params = dict()
    params['phone'] = '+7 (991) 366-60-60'
    params['email'] = 'my-longhair@mail.ru'
    params['address'] = 'г. Ростов-на-Дону, Нахичевань, 30-я Линия д.15'
    params['vk_group'] = 'https://vk.com/narashchivanie_rostov'
    return render_template('contacts.html', **params)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('/')
        return render_template('login.html',
                               message='Неверный логин или пароль',
                               title='Ошибка авторизации',
                               form=form)

    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = Register()
    if form.validate_on_submit():  # то же самое, что и request.method == 'POST'
        # если пароли не совпали
        if form.password.data != form.password_again.data:
            return render_template('register.html',
                                   title='Регистрация',
                                   message='Пароли не совпадают',
                                   form=form)

        db_sess = db_session.create_session()

        # Если пользователь с таким E-mail в базе уже есть
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html',
                                   title='Регистрация',
                                   message='Такой пользователь уже есть',
                                   form=form)
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )

        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html',
                           title='Регистрация', form=form)

@app.route('/countdown')
def cd():
    lst = [str(i) for i in reversed(range(10))]
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
@app.route('/get-users/')
@app.route('/get-users/<int:id_num>')
def get_users(id_num=None):
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


# тянем с базы по определённым условиям и отображаем на странице
# если id нет, то выводим список ссылок существующих позиций
@app.route('/get-user/')
@app.route('/get-user/<int:id_num>')
def get_user(id_num=None):
    try:
        # Подключение к базе данных
        con = sqlite3.connect('db/movies.sqlite')
        cur = con.cursor()

        if id_num is None:
            # Получение списка всех пользователей
            query = 'SELECT trip_id, name FROM users'
            response = cur.execute(query)
            result = response.fetchall()
            return render_template('get_user.html', users=result)

        # Получение информации о конкретном пользователе
        query = 'SELECT name, city, date_first FROM users WHERE trip_id=?'
        response = cur.execute(query, (id_num,))
        result = response.fetchone()

        if result:
            name, city, date_first = result
            return render_template('get_user.html',
                                   name=name,
                                   city=city,
                                   start=date_first)
        else:
            return "Пользователь не найден", 404

    except Error as e:
        return f"Произошла ошибка: {str(e)}", 500

    finally:
        # Гарантированное закрытие соединения
        if con:
            cur.close()
            con.close()



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


@app.route('/news')
def news():
    db_sess = db_session.create_session()
    all_news = db_sess.query(News).filter(News.is_private == False).all()
    return render_template('news.html', title='Новости',
                                                          news=all_news)
# добавление новой пользователя в таблицу SQL
# локальный хост - 127.0.0.1
if __name__ == '__main__':
    db_session.global_init('db/news.sqlite')
    app.run(host='localhost', port=5000, debug=debug)
#     user = User()
#     user.name = 'User2'
#     user.about = 'Данные про User2'
#     user.email = 'b@b.ru'
#     db_sess = db_session.create_session()
#     db_sess.add(user)
#     db_sess.commit()

# # вытаскиваем конкретного пользователя
# # локальный хост - 127.0.0.1
# if __name__ == '__main__':
#     db_session.global_init('db/news.sqlite')
#     # app.run(host='localhost', port=5000, debug=debug)
#     user = User() # создаём образ объекта
#     db_sess = db_session.create_session() # подключаемся к базе
#     first = db_sess.query(User).filter((User.id == 1) & User.email.not_like('%a%')).all()  # условие
#     print (first)

# # найти конкретного юсера и поменять ему имя
# # локальный хост - 127.0.0.1
# if __name__ == '__main__':
#     db_session.global_init('db/news.sqlite')
#     db_sess = db_session.create_session() # подключаемся к базе
#     user = db_sess.query(User).filter(User.id == 2).first()  # условие
#     user.set_username('Billy')
#     db_sess.commit()
#     print (user)

# # удалить конкретную запись
# # локальный хост - 127.0.0.1
# if __name__ == '__main__':
#     db_session.global_init('db/news.sqlite')
#     db_sess = db_session.create_session() # подключаемся к базе
#     user = db_sess.query(User).filter(User.id == 2).first()  # условие
#     if user:
#         db_sess.delete(user)
#         print(f'Пользователя с id {2} удалили из базы')
#     else:
#         print(f'Пользователя с id {2} не существует')
#     db_sess.commit()


# добавление новости в таблицу SQL
# локальный хост - 127.0.0.1
# if __name__ == '__main__':
#     db_session.global_init('db/news.sqlite')
#     # app.run(host='localhost', port=5000, debug=debug)
#     news = News()
#     news.title = 'Новость1'
#     news.content = 'Описание новости'
#     news.user_id = '1'
#     db_sess = db_session.create_session()
#     db_sess.add(news)
#     db_sess.commit()
# # добавление новости в таблицу SQL = 2й вариант
# if __name__ == '__main__':
#     db_session.global_init('db/news.sqlite')
#     db_sess = db_session.create_session()
#     user = db_sess.query(User).filter(User.id == 1).first()
#     news = News(title='Second News', content='News Content',
#                 user_id=user.id, is_private=False)
#     db_sess.add(news)
#     db_sess.commit()
#
# # получить конкретную новость конкретного пользователя
# if __name__ == '__main__':
#     db_session.global_init('db/news.sqlite')
#     db_sess = db_session.create_session()
#     user = db_sess.query(User).filter(User.id == 1).first()
#     for news in user.news:
#         if news.id == 2:
#             print(news)
