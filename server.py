#!/usr/bin/python

import json

from euler import EulerPrimeFinder
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_pair', methods=['GET'])
def pair():
	finder = EulerPrimeFinder(1000)
	count_the_two = True if request.args.get('count_the_two', '') == 'on' else False
	try:
		results = finder.find_xth_prime_of_y_digits(
			int(request.args.get('x', 0)),
			int(request.args.get('y', 0)),
			count_the_two)
	except ValueError:
		return render_template('index.html')
	return render_template('index.html', results=json.dumps(results))

if __name__ == '__main__':
    app.run()