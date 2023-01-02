from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def score_game():
    return render_template("scores.game.html")

def score_error():
    return render_template("scores.error.html")


app.run('0.0.0.0')