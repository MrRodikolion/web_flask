from flask import Flask

app = Flask(__name__)


@app.route('/')
def mision_name():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Колонизация Марса</title>
                  </head>
                  <body class="d-flex h-100 text-center text-bg-dark">
                    <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
                      <header class="mb-auto"></header>

                      <main class="px-3">
                        <h3>Название миссии</h3>
                        <p class="lead">Миссия Колонизация Марса</p>
                      </main>
                    </div>
                  </body>
                </html>'''


@app.route('/index')
def losund():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Колонизация Марса</title>
                  </head>
                  <body class="d-flex h-100 text-center text-bg-dark">
                    <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
                      <header class="mb-auto"></header>

                      <main class="px-3">
                        <h1>Девиз миссии</h1>
                        <p class="lead">И на Марсе будут яблони цвести!</p>
                      </main>
                    </div>
                  </body>
                </html>'''


@app.route('/promotion')
def promotion():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Колонизация Марса</title>
                  </head>
                  <body class="d-flex h-100 text-center text-bg-dark">
                    <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
                      <header class="mb-auto"></header>

                      <main class="px-3">
                        <h1>Рекламная кампания</h1>
                        <p class="lead">Человечество вырастает из детства.
                                        <br>
                                        Человечеству мала одна планета.
                                        <br>
                                        Мы сделаем обитаемыми безжизненные пока планеты.
                                        <br>
                                        И начнем с Марса!
                                        <br>
                                        Присоединяйся!</p>
                      </main>
                    </div>
                  </body>
                </html>'''


@app.route('/image_mars')
def img_mars():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body class="d-flex h-100 text-center text-bg-dark">
                    <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
                      <header class="mb-auto"></header>

                      <main class="px-3">
                        <h1>Жди нас, Марс!</h1>
                        <img src='/static/img/mars.jpg'>
                      </main>
                    </div>
                  </body>
                </html>'''


@app.route('/promotion_image')
def promotion_image():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="static/css/style.css" />
                    
                    <title>Колонизация Марса</title>
                  </head>
                  <body class="d-flex h-100 text-center text-bg-dark">
                    <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
                      <header class="mb-auto"></header>

                      <main class="px-3">
                        <h1>Рекламная кампания</h1>
                        <img src='/static/img/mars.jpg'>
                        <p class="lead">Человечество вырастает из детства.
                                        <br>
                                        Человечеству мала одна планета.
                                        <br>
                                        Мы сделаем обитаемыми безжизненные пока планеты.
                                        <br>
                                        И начнем с Марса!
                                        <br>
                                        Присоединяйся!</p>
                      </main>
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
