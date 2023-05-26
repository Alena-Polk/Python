from flask import Flask, render_template, url_for, request, flash, session, g, redirect, abort
import os
import sqlite3
from FDataBase import FDataBase

DATABASE = '/tmp/shop.db'
DEBUG = True
SECRET_KEY = '4b417b07170153bb8bcf26c3233ff4d0aab2e096'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'shop.db')))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


menu = [
    {"name": "Главная", "url": "index"},
    {"name": "Каталог", "url": "shop"},
    {"name": "О компании", "url": "company"},
    {"name": "Акции", "url": "stock"},
    {"name": "Контакты", "url": "contact"},
]


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
@app.route("/catalog")
def catalog():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('catalog.html', title="Товары дня", menu=dbase.get_menu(), posts=dbase.get_posts_anonce())


@app.route("/inform")
def inform():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('inform.html', title="Информация", menu=dbase.get_menu())


@app.route("/add_product", methods=["POST", "GET"])
def add_product():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == 'POST':
        if len(request.form['name']) > 2 and len(request.form['post']) > 10:
            res = dbase.add_post(request.form['name'], request.form['price'], request.form['post'])
            if not res:
                flash('Ошибка добавления товара', category='error')
            else:
                flash('Товар добавлен успешно', category='success')
        else:
            flash('Ошибка добавления товара', category='error')
    return render_template('add_product.html', title="Добавление товара", menu=dbase.get_menu())


@app.route('/post/<int:id_post>')
def show_post(id_post):
    db = get_db()
    dbase = FDataBase(db)
    title, price, post = dbase.get_post(id_post)
    if not title:
        abort(404)
    return render_template('post.html', title=title, price=price, post=post, menu=dbase.get_menu())


@app.route("/index")
def index():
    db = get_db()
    return render_template('index.html', title="Главная", menu=menu)


@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"


@app.route("/shop")
def shop():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('shop.html', title="Категории товаров", menu=dbase.get_menu())


@app.route("/company")
def company():
    return render_template('company.html', title="О компании", menu=menu)


@app.route("/stock")
def stock():
    return render_template('stock.html', title="Все акции", menu=menu)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        if len(request.form['message']) > 2:
            flash('Сообщение отправлено успешно', category='success')
        else:
            flash('Ошибка отправки', category='error')
        context = {
            'username': request.form['username'],
            'email': request.form['email'],
            'message': request.form['message']
        }
        return render_template('contact.html', title="Контакты", menu=menu, **context)
    return render_template('contact.html', title="Контакты", menu=menu)


@app.route('/login', methods=["POST", "GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'elena' and request.form['psw'] == 'rnch4hzf7':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html', title="Авторизация", menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template('page404.html', title='Страница не найдена', menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run(debug=True)


