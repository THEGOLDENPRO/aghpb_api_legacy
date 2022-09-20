import flask

app = flask.Flask(__name__)

from . import chiitan, random

@app.get("/api")
def root():
    return "uwu"

def run():
    app.run()