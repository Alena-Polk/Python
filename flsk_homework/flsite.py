from flask import Flask, render_template, url_for, request

app = Flask(__name__)

menu = [
    {"name": "О нас", "url": "index"},
    {"name": "Режим работы", "url": "about"},
    {"name": "Обратная связь", "url": "contact"},
]


@app.route("/index")
@app.route("/")
def index():
    print(url_for('index'))
    return render_template('index.html', title="Общая информация", menu=menu)


@app.route("/about")
def about():
    print(url_for('about'))
    return render_template('about.html', title="Информация", menu=menu)


@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        print(request.form)
        context = {
            'username': request.form['username'],
            'email': request.form['email'],
            'massage': request.form['massage']
        }
        return render_template("contact.html", title="Обратная связь", menu=menu, **context)
    return render_template("contact.html", title="Обратная связь", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
