import os
import sys

from flask import Flask
from flask import logging
from flask import make_response
from flask import render_template
from flask import request

import config

app = Flask(__name__)

here = os.path.abspath(os.path.dirname(__file__))

if "/" in config.STARTING_DIRECTORY:
    base_directory = ""
else:
    base_directory = config.STARTING_DIRECTORY

if "/" not in config.STARTING_DIRECTORY:
    config.STARTING_DIRECTORY = os.path.join(here, config.STARTING_DIRECTORY)


def get_structure(directory):
    return os.walk(directory).__next__()


def display_files(files):
    keep_files = []
    for file in files:
        for file_type in config.FILE_TYPES:
            if file_type in file:
                keep_files.append(file)
    return keep_files


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        root, directories, files = get_structure(config.STARTING_DIRECTORY)
        return render_template("index.html", display_root=root[root.find(base_directory):], root=root,
                               directories=directories, files=display_files(files))

    if "file" in request.args:
        root, directory, file = request.args["root"], request.args["directory"], request.args["file"]
        pdf = os.path.join(root, directory, file)
        with open(pdf, 'rb') as pdf_file:

            response = make_response(pdf_file.read())
            response.headers['Content-Type'] = 'application/pdf'
            response.headers['Content-Disposition'] = "inline; filename={}".format(file)
            return response

    root, directories, files = get_structure(os.path.join(request.args["root"], request.args["directory"]))
    return render_template("index.html", display_root=root[root.find(base_directory):], root=root,
                           directories=directories, files=display_files(files))

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5555,
        debug=False,
        threaded=False,
    )
