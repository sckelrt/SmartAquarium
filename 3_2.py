import json
from data import db_session
from flask import Flask, render_template, redirect
from data.SavingData import SavingData


SavingDataManager = SavingData()
app = Flask(__name__)

aquariumParametres = {'temp': (27, 30), 'humidity': (90, 99), 'temp2': (24, 26), 'PH': (6, 8.5), 'volt': (1, 2),
                      'light': (100, 200)}

def dataSave(data):
    SavingDataManager.temp_air = data[0]
    SavingDataManager.humidity = data[1]
    SavingDataManager.temp_water = data[2]
    SavingDataManager.PH = data[3]
    SavingDataManager.volt = data[4]
    SavingDataManager.water = data[5]
    SavingDataManager.light = data[6]
    SavingDataManager.LIGH = data[7]
    SavingDataManager.Cooling = data[8]
    db_sess = db_session.create_session()
    db_sess.add(SavingDataManager)
    db_sess.commit()

@app.route('/')
def index():
    return redirect('/data')


@app.route('/data')
def data():
    DataContanier = []
    RGBparamemtres = list()
    with open("templates/data.json", "rt", encoding="utf8") as f:
        data_list = json.loads(f.read())
        for data in data_list:
            try:
                if aquariumParametres[data][0] < float(data_list[data]) < aquariumParametres[data][1]:
                    RGBparamemtres.append("alert-success")
                    DataContanier.append(data_list[data])
                else:
                    RGBparamemtres.append("alert-danger")
                    DataContanier.append(data_list[data])
            except:
                print('false')
                DataContanier.append(data_list[data])
    dataSave(DataContanier)
    return render_template('data.html', data_list=data_list, RGBparamemtres=RGBparamemtres)


@app.route('/news')
def news():
    return render_template('news.html')


if __name__ == '__main__':
    db_session.global_init("db/AquariumData.db")
    app.run(port=8081, host='127.0.0.1')
