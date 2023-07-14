from flask import Flask, render_template

app = Flask(__name__)

menu = [
    {'name': 'Главная', 'url': 'index'},
    {'name': 'Галерея', 'url': 'gallery'},
    {'name': 'Услуги и цены', 'url': 'price'},
    {'name': 'Обратная связь', 'url': 'contacts'},
]


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', title='Главная', menu=menu)


@app.route('/gallery')
def gallery():
    return render_template('gallery.html', title='Галерея', menu=menu)


@app.route('/price')
def price():
    return render_template('price.html', title='Услуги и цены', menu=menu)


@app.route('/contacts')
def contacts():
    return render_template('contacts.html', title='Обратная связь', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
