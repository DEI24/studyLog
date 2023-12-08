from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def studyLog():
    return render_template('index.html')

