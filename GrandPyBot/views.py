from flask import Flask, render_template, request, jsonify
from GrandPyBot.system import System
import sys, json

app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask/', methods=['POST'])
def launch():
	if request.method == 'POST':
		data = request.form['question']
		system = System(data)
		dict_sys = system.questionning()
		return dict_sys
	else:
		return "Oups il y a un bug dans la matrice."

if __name__ == "__main__":
    app.run()