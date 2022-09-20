import flask
from flask import send_from_directory, Response, request

app = flask.Flask(__name__)
app.config.from_pyfile("../flask-instance/config.py")

API_NAME = "AGHPB"
API_PATH = f"/{API_NAME.lower()}"

from . import programing_books
from . import chiitan, random, language, languages_list

@app.get(API_PATH + "/")
def root():
    return send_from_directory("../files", "index.html")

@app.before_request
def print_the_request():
    print(f"[{request.remote_addr}] ({request.url_root}) [{request.method}]")

@app.after_request
def add_header(r:Response):
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate, public, max-age=0'
    return r

def run():
    app.run()