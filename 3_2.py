import json

from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/data')
def member():
    with open("templates/data.json", "rt", encoding="utf8") as f:
        data_list = json.loads(f.read())
    return render_template('member.html', data_list=data_list)


@app.route('/')
def index():
    return redirect('/data')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
