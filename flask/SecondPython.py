from flask import Flask

from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello! This is the main page <h1> HELLO <H1>"

@app.route('/name')
def name():
    name = "Mark Jigger"
    return """<html><body>
    <h1>Hello, my name is {0}</h1>
    </body><html>""".format(name)

    # Launch the Flask dev server
    app.run(host="localhost", debug=True)


if __name__ == '__main__':
    app.run()
