from xml.sax.saxutils import escape
from markupsafe import escape

from flask import Flask, jsonify, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/hello/<name>')
def groeten(name):
    return f"Hello {escape(name)}"

@app.route('/greetsfrom/<name>')
def greetsfrom(name):
    return render_template("greetsfrom.html", name=escape(name))