from . import app

from flask import send_from_directory

@app.get("/api/random")
def random():
    return send_from_directory("../files", "lets_play_chiitan.mp4")