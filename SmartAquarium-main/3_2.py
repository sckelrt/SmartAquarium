import json

from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

aquariumParametres = {'temp': (27, 30), 'humidity': (90, 99), 'temp2': (24, 26), 'PH': (6, 8.5), 'volt': (1, 2),
                      'light': (100, 200)}


@app.route('/')
def index():
    return redirect('/data')


@app.route('/data', methods=['POST', 'GET'])
def data():
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
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Пример формы</title>
                              </head>
                              <body>
                                <h1>Форма для регистрации в суперсекретной системе</h1>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                        <button type="submit" class="btn btn-primary">Записаться</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['password'])
        RGBparamemtres = list()
        with open("templates/data.json", "rt", encoding="utf8") as f:
            data_list = json.loads(f.read())
            for data in data_list:
                try:
                    if aquariumParametres[data][0] < float(data_list[data]) < aquariumParametres[data][1]:
                        RGBparamemtres.append("alert-success")
                    else:
                        RGBparamemtres.append("alert-danger")
                except:
                    print('false')
        return render_template('data.html', data_list=data_list, RGBparamemtres=RGBparamemtres,
                               password=request.form['password'])


@app.route('/news')
def news():
    return render_template('news.html')


@app.route('/project')
def project():
    return render_template('project.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/form_sample', methods=['POST', 'GET'])
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
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации в суперсекретной системе</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['password'])
        RGBparamemtres = list()
        with open("templates/data.json", "rt", encoding="utf8") as f:
            data_list = json.loads(f.read())
            for data in data_list:
                try:
                    if aquariumParametres[data][0] < float(data_list[data]) < aquariumParametres[data][1]:
                        RGBparamemtres.append("alert-success")
                    else:
                        RGBparamemtres.append("alert-danger")
                except:
                    print('false')
        return render_template('data.html', data_list=data_list, RGBparamemtres=RGBparamemtres,
                               password=request.form['password'])


if __name__ == '__main__':
    app.run(port=8081, host='127.0.0.1')
