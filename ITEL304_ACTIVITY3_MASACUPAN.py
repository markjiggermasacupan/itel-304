from flask import Flask, request
from datetime import datetime

app = Flask(__name__)


@app.route('/')
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

    username = request.args.get('username', '')
    characteristic = request.args['characteristic', '']
    if username == '' and characteristic == '':
        msg = 'Invalid input, you do not input your username and characteristic'

        username = request.args.get('username', '')
        characteristic = request.args['characteristic', '']
    elif username == '' or characteristic == '':
        msg = 'Invalid input, you do not input your username and characteristic'

        username = request.args.get('username')
        characteristic = request.args['characteristic', '']
    elif characteristic == '':
        msg = 'Your characteristic is unknown, please enter!'

        username = request.args.get('username', '')
        characteristic = request.args['characteristic']
    elif username == '':
        msg = 'You do not input your name, please enter!'

        username = request.args.get('username')
        characteristic = request.args['characteristic']
    else:
        msg = 'You are' + characteristic

    return """
        <html><body>
            <h2>Hello, {0}!</h2>
            <p> You are {1}</p>
      </body></html>
      """.format(username, msg)


# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)
