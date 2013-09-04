#!/usr/bin/env python3

from flask import Flask, render_template, url_for, request, send_from_directory
import pylab
import io
import base64
import stronghold


app = Flask(__name__)


@app.route('/plot', methods=['GET', 'POST'])
def plot():
    data = {}
    data['form'] = request.form
    if request.method == 'POST':
        data['locations'] = stronghold.guess_locations((float(request.form['x']), float(request.form['z'])))
        x = []
        y = []
        for i in data['locations']:
            x.append(i[0])
            y.append(i[1])
        pylab.scatter(x, y)
        buf = io.BytesIO()
        pylab.savefig(buf, format='png')
        buf.seek(0)
        data['plot'] = base64.b64encode(buf.read())
        buf.close()
    return render_template('plot.html', data=data)


@app.route('/locate', methods=['GET', 'POST'])
def locate():
    location = {}
    location['form'] = request.form

    if request.method == 'POST':
        location1 = (float(request.form['x1']), float(request.form['z1']),
                     float(request.form['f1']))
        location2 = (float(request.form['x2']), float(request.form['z2']),
                     float(request.form['f2']))
        location['1'] = location1
        location['2'] = location2
        location['result'] = stronghold.locate(location1, location2)
    return render_template('locate.html', location=location)


@app.route('/')
def index():
    return send_from_directory('static', filename='homepage.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
