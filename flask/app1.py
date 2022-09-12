from flask import Flask

from datetime import datetime

app = Flask(__name__)


@app.route('/')

def hello():
    return """<html><body>
    <h1>Hello, World!</h1>
    The time is {0}.</body><html>""".format(str(datetime.now()))

    # Launch the Flask dev server
    app.run(host="localhost", debug=True)


if __name__ == '__main__':
    app.run()
