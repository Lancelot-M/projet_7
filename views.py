from flask import Flask, render_template, request, jsonify
from GrandPyBot.test import Wiki_api
#import sys

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test/', methods=['GET', 'POST'])
def wiki_test():
	if request.method == 'POST':
		question = request.form['question']
		#print(question, file=sys.stderr)
		answer = Wiki_api.load_page(question)
		data = [question, answer]
		return jsonify(data)
	else:
		return "Oups il y a un bug dans la matrice."

if __name__ == "__main__":
    app.run()