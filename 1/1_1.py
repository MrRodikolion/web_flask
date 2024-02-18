from flask import Flask, request
from pprint import pprint

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


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="static/css/form.css" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <div class="py-5 text-center">
                              <h2>Анкета претендента</h2>
                              <p class="lead">на участие в миссии</p>
                            </div>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="last-name" class="form-control" id="last-name" placeholder="Фамилия" name="last-name">
                                    <input type="fist-name" class="form-control" id="fist-name" placeholder="Имя" name="fist-name">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="education-select">Какое у вас образование</label>
                                        <select class="form-control" id="education" name="education">
                                          <option>Глупое</option>
                                          <option>Обычное</option>
                                          <option>Норм</option>
                                          <option>Крутое</option>
                                          <option>Мега Крутое</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="form-check">Выбор основной профессии</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="meh" value="meh" checked>
                                          <label class="form-check-label" for="meh">
                                            Маханик
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="pro" value="pro" checked>
                                          <label class="form-check-label" for="pro">
                                            Крутой
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="clown" value="clown" checked>
                                          <label class="form-check-label" for="clown">
                                            Клоун
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужчина
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="promale" value="promale" checked>
                                          <label class="form-check-label" for="promale">
                                            Накачанный Мужчина
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы тут</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов служить</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        pprint(request.form)
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
