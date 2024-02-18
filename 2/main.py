from flask import Flask, request, render_template
from pprint import pprint
import requests

app = Flask(__name__)


@app.route('/<title>')
def index(title):
    params = {
        'title': title
    }
    return render_template('index.html', **params)


@app.route('/training/<prof>')
def prof(prof):
    prof = prof.lower()
    type = 'Научные симуляторы'
    if 'строитель' in prof or 'инженер' in prof:
        type = 'Инженерные тренажеры'

    params = {
        'title': prof,
        'type': type,
        'path': '/static/img/plan.jpg'
    }
    return render_template('prof.html', **params)


@app.route('/list_prof/<ltype>')
def list_prof(ltype):
    params = {
        'title': 'Список профессий',
        'ltype': ltype,
        'prof_list': ['Астронавт-исследователь',
                      'Инженер-космонавт',
                      'Биолог',
                      'Химик',
                      'Геолог',
                      'Метеоролог',
                      'Пилот космического корабля',
                      'Инженер по связи',
                      'Инженер по жизнеобеспечению',
                      'Психолог']
    }
    return render_template('list_prof.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
