#!/usr/bin/python

import json

from csv import DictReader
from euler import EulerPrimeFinder
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	"""
	Handles the naked/initial page.
	"""
	return render_template('index.html')

@app.route('/submit_pair', methods=['GET'])
def pair():
	"""
	Handles single-pair requests.
	"""
	finder = EulerPrimeFinder(1000)
	count_the_two = True if request.args.get('count_the_two', '') == 'on' else False
	try:
		results = finder.find_xth_prime_of_y_digits(
			int(request.args.get('x', 0)),
			int(request.args.get('y', 0)),
			count_the_two)
	except ValueError:
		# We got something that wasn't a valid int, so nothing we can do but fall back
		return render_template('index.html')
	return render_template('index.html', results=json.dumps([results]))

@app.route('/submit_file', methods=['POST'])
def upload():
	"""
	Handles uploads containing multiple pairs of requests.
	"""
	finder = EulerPrimeFinder(1000)
	reader = DictReader(request.files['uploaded_csv'], ['x', 'y'])

	multiple_results = []

	for row in reader:
		try:
			multiple_results.append(
				finder.find_xth_prime_of_y_digits(int(row['x']), int(row['y']), False))
		except ValueError:
			continue

	return render_template('index.html', results=json.dumps(multiple_results))

if __name__ == '__main__':
    app.run()