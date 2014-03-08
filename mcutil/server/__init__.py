#!/usr/bin/env python

from flask import Flask, render_template, request
import matplotlib
matplotlib.use('Agg')  # Work without a display.
from matplotlib import pyplot as plt
import io
import base64
from mcutil.common import simplify, Point, Vector
import mcutil.stronghold as stronghold


app = Flask(__name__)
parse_int = lambda n: simplify(float(n))

@app.route('/plot', methods=['GET', 'POST'])
def plot():
    data = {}
    data['form'] = request.form
    if request.method == 'POST':
        plt.clf()  # Clear plot data left over from previous requests.
        known_location = Point(parse_int(request.form['x']),
                               parse_int(request.form['z']))
        data['locations'] = stronghold.guess_locations(known_location)
        x, y = zip(*data['locations'])
        plt.scatter(x, y)
        with io.BytesIO() as buf:
            plt.savefig(buf, format='png')
            buf.seek(0)
            data['plot'] = base64.b64encode(buf.read())
    return render_template('plot.html', data=data)


@app.route('/locate', methods=['GET', 'POST'])
def locate():
    location = {}
    location['form'] = request.form

    if request.method == 'POST':
        location['1'] = Vector(parse_int(request.form['x1']),
                               parse_int(request.form['z1']),
                               float(request.form['f1']))
        location['2'] = Vector(parse_int(request.form['x2']),
                               parse_int(request.form['z2']),
                               float(request.form['f2']))
        location['result'] = stronghold.locate(location['1'], location['2'])
    return render_template('locate.html', location=location)


@app.route('/')
def index():
    return app.send_static_file('homepage.html')
