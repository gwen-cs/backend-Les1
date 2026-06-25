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

@app.route ("/som/<int:a>/<int:b>")
def som(a,b):
    return f"<h1>De som van deze twee is: {a + b}</H1>"

@app.route ("/persoon/<string:naam>/<int:leeftijd>")
def persoon (naam, leeftijd):
    return f"<h1>{escape(naam)} is {escape(leeftijd)} jaar oud ! </h1>"

@app.route ("/id/<string:id_voornaam>/<string:id_achternaam>/<int:id_nummer>")
def id (id_voornaam, id_achternaam, id_nummer):
    return (f"""
            <H1> resultaat </h1>
            <p>Voornaam = {escape(id_voornaam)}</p>
            <p>Achternaam = {escape(id_achternaam)}</p>
            <p>ID_nummer = {escape(id_nummer)}</p>
    """)

@app.route ("/auto/<string:merk>/<string:type>/<string:kleur>/<int:PK>")
def auto (merk, type, kleur, PK):
    return render_template("auto.html", merk=escape(merk), type=escape(type), kleur=escape(kleur), PK=escape(PK))

@app.route ("/student/<string:naam>/<int:leeftijd>/<string:richting>")
def student (naam, leeftijd, richting):
    return render_template("student.html", naam=escape(naam), leeftijd=escape(leeftijd), richting=escape(richting))

@app.route ("/reis/<path:reisbestemming>")
def reisbestemming (reisbestemming):
    return render_template("reis.html", reisbestemming=escape(reisbestemming))