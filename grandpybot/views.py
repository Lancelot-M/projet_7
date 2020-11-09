"""File containing routes of the app."""

from flask import Flask, render_template, request
from grandpybot.system import System

app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
def home():
    """Home page route."""
    return render_template('index.html')

@app.route('/ask/', methods=['POST'])
def launch():
    """Chat with bot's route."""
    if request.method == 'POST':
        data = request.form['question']
        system = System(data)
        dict_sys = system.questionning()
        return dict_sys
    return "Oups il y a un bug dans la matrice."

if __name__ == "__main__":
    app.run()
