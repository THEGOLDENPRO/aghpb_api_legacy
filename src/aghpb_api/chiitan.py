from . import app, API_PATH

from flask import send_from_directory

@app.get(API_PATH + "/chiitan")
def chiitan():
    return send_from_directory("../files", "lets_play_chiitan.mp4")