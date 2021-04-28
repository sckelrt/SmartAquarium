import json
from data import db_session
from flask import Flask, render_template, redirect
from data.SavingData import SavingData
from apscheduler.schedulers.background import BackgroundScheduler

SavingDataManager = SavingData()
app = Flask(__name__)

aquariumParametres = {'temp': (27, 30), 'humidity': (90, 99), 'temp2': (24, 26), 'PH': (6, 8.5), 'volt': (1, 2),
                      'light': (100, 200)}


def dataSave():
    aquariumID = 0  # вставишь тут поле с id
    DataContanier = []
    with open("templates/data.json", "rt", encoding="utf8") as f:
        data_list = json.loads(f.read())
        for jsonData in data_list:
            DataContanier.append(data_list[jsonData])
    db_sess = db_session.create_session()
    print((db_sess.query(SavingData).order_by(SavingData.id)[-1]))
    DataContanier.append(aquariumID)
    SavingDataManager.id = + 1
    SavingDataManager.temp_air = DataContanier[0]
    SavingDataManager.humidity = DataContanier[1]
    SavingDataManager.temp_water = DataContanier[2]
    SavingDataManager.PH = DataContanier[3]
    SavingDataManager.volt = DataContanier[4]
    SavingDataManager.water = DataContanier[5]
    SavingDataManager.light = DataContanier[6]
    SavingDataManager.LIGH = DataContanier[7]
    SavingDataManager.Cooling = DataContanier[8]
    SavingDataManager.aquarium_id = aquariumID
    db_sess.add(SavingDataManager)
    db_sess.commit()


@app.route('/')
def index():
    return redirect('/data')


@app.route('/data')
def data():
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
    return render_template('data.html', data_list=data_list, RGBparamemtres=RGBparamemtres)


@app.route('/news')
def news():
    return render_template('news.html')


sched = BackgroundScheduler(daemon=True)
sched.add_job(dataSave, 'interval', seconds=5)
sched.start()

if __name__ == '__main__':
    db_session.global_init("db/AquariumData.db")
    app.run(port=8081, host='127.0.0.1')
