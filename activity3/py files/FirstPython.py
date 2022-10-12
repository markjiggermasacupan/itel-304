from flask import Flask

from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <html><body>
        <h1>Hello, World!</h1>
        Click <a href="/time">here</a>for the time.
        </body><html>"""

@app.route('/time')
def time():
    # Launch the Flask dev server
    app.run(host="localhost", debug=True)


if __name__ == '__main__':
    app.run()
