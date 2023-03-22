from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/habilidades")
def habilidades():
    return render_template("habilidades.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/video_game")
def video_game():
    return render_template("/video_game.html")

@app.route("/video_device")
def video_device():
    return render_template("/video_device.html")
