#!/usr/bin/env python3

from flask import Flask, render_template, request, send_from_directory
import matplotlib
matplotlib.use('Agg')  # Work without a display.
from matplotlib import pyplot as plt
import io
import base64
import stronghold


app = Flask(__name__)


@app.route('/plot', methods=['GET', 'POST'])
def plot():
    data = {}
    data['form'] = request.form
    if request.method == 'POST':
        known_location = stronghold.Location(float(request.form['x']),
                                             float(request.form['z']))
        data['locations'] = stronghold.guess_locations(known_location)
        x, y = zip(*data['locations'])
        plt.scatter(x, y)
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        data['plot'] = base64.b64encode(buf.read())
        buf.close()
    return render_template('plot.html', data=data)


@app.route('/locate', methods=['GET', 'POST'])
def locate():
    location = {}
    location['form'] = request.form

    if request.method == 'POST':
        location['1'] = stronghold.Vector(float(request.form['x1']),
                                          float(request.form['z1']),
                                          float(request.form['f1']))
        location['2'] = stronghold.Vector(float(request.form['x2']),
                                          float(request.form['z2']),
                                          float(request.form['f2']))
        location['result'] = stronghold.locate(location['1'], location['2'])
    return render_template('locate.html', location=location)


@app.route('/')
def index():
    return send_from_directory('static', filename='homepage.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
