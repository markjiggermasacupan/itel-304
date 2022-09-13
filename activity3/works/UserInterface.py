from flask import Flask, request
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello():
    return """<html><body>
    <h1>Hello, World!</h1>
    Click <a href="/time">here</a> for the time.
    </body></html>
    """


@app.route('/time')
def time():
    return """
    <html><body>
    The time is {0}.
    Click <a href="/Engaging Activities">here</a> for the proceedings.
    </body></html>
    """.format(str(datetime.now()))


@app.route('/Engaging Activities')
def home():
    return """
    <html><body>
        <h2> Welcome Man!</h2>
        <form action="/greet">
            Your full name {0} <input type='text' name='fname'><br>
            And your characteristic {0} <input type='text' name='characteristic'><br>
            <input type='submit' value='Continue'>
        </form>
    </body><html>
    """.format("is")


@app.route("/greet")
def greet():

    username = request.args.get('username', 'Mark Jigger Masacupan')
    characteristic = request.args['characteristic', ]

    if characteristic == '' and username == '':
        msg = 'Invalid input, you do not input your characteristic and username'
        if username == '' != characteristic == '':
            msg = 'Invalid input, you do not input your username' + characteristic
        else:
            msg = 'You do not enter your name' + ' I am ' + characteristic
    else:
        msg = 'My name is ' + username + \
            ' and I am ' + characteristic

    return """
        <html><body>
            <h2>Hello, {0}!</h2>
            {1}
      </body></html>
      """.format(username, msg, "is")


# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)
