# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def introduction():
    return render_template('index.html', active_page='index')

@app.route('/types_of_cybersecurity')
def types_of_cybersecurity():
    return render_template('types_of_cybersecurity.html', active_page='types_of_cybersecurity')

@app.route('/cybersecurity_threats')
def cybersecurity_threats():
    return render_template('cybersecurity_threats.html', active_page='cybersecurity_threats')

@app.route('/action')
def action():
    return render_template('action.html', active_page='action')

if __name__ == "__main__":
    app.run(debug=True)
