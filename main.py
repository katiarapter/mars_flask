from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def title():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def motto():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    agitation = ['Даёшь новые горизонты!',
                 'Даёшь уменьшение риска вымирания человечества!',
                 'Даёшь колонизацию Марса!']
    return '</br>'.join(agitation)


@app.route('/image_mars')
def image():
    return """<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{}" alt="Здесь должна быть картинка, но ее нет....">
                    <p>Вот она какая, красная планета</p>
                  </body>
                </html>""".format(url_for('static', filename='mars.jpg'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
