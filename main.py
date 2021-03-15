from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask()
db = SQLAlchemy(app)

@app.route ('/server')
def server():
    context = {"something":"something_text"}
    return render_template("index.html", **context)