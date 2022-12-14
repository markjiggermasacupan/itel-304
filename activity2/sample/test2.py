from flask import Flask, request

from datetime import datetime

app = Flask(__name__)


@app.route('/home')
def home():
    return """
    <html><body>
        <h4> Welcome to the Greeter</h4>
        <form action="/greet">
            Your full name {0} <input type='text' name='fname'><br>
            And your characteristic  {0} <input type='text' name='char'><br>
            <input type='submit' value='Continue'>
        </form>
    </body><html>
    """.format("is")


@app.route("/greet")
def greet():
    fname = request.args.get('fname')
    char = request.args['char']
    if char == '':
        msg = 'How can I know you, if you do not tell your name?'
    else:
        msg = 'Your name' + {0} + fname + \
            'and your characteristic' + {0} + char

    return """
        <html><body>
            <h2>Hello {0}!</h2>
            {1}
      </body></html>
      """.format(fname, msg, "is")


# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)
