import json

from flask import Flask, render_template, redirect

app = Flask(__name__)

aquariumParametres = {'temp': (27, 30), 'humidity': (90, 99), 'temp2': (24, 26), 'PH': (6, 8.5), 'volt': (1, 2),
                      'light': (100, 200)}


@app.route('/data')
def member():
    RGBparamemtres = list()
    with open("templates/data.json", "rt", encoding="utf8") as f:
        data_list = json.loads(f.read())
        for data in data_list:
            if aquariumParametres[data][0] < data < aquariumParametres[data][1]:
                RGBparamemtres.append(f'0.{int(data) * 3}.77')
    return render_template('member.html', data_list=data_list)


@app.route('/')
def index():
    return redirect('/data')


if __name__ == '__main__':
    app.run(port=8081, host='127.0.0.1')
