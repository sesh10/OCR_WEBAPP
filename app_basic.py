import os
from flask import Flask, render_template, request

__author__ = 'ibininja'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")



@app.route("/upload")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'ImageOCR/images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return render_template("complete.html")





@app.route("/uploadpdf")
def indexpdf():
    return render_template("uploadpdf.html")

@app.route("/uploadpdf", methods=['POST'])
def uploadpdf():
    target = os.path.join(APP_ROOT, 'PDF/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return render_template("complete.html")




@app.route("/uploadform")
def indexform():
    return render_template("uploadform.html")

@app.route("/uploadform", methods=['POST'])
def uploadform():
    target = os.path.join(APP_ROOT, 'forms/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return render_template("complete.html")



if __name__ == "__main__":
    app.run(port=5000, debug=True)