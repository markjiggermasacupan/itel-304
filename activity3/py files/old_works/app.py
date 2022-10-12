from codecs import charmap_decode
from flask import Flask, request

from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    return """
    <html><body>
        <h4> ITEL 304 (Integrative and Programming Technologies 2) </h4>
        <form action="/greet">
            Your full name {0} <input type='text' name='fname'><br>
            And your characteristic  {0} <input type='text' name='char'><br>
            <input type='submit' value='Continue'>
        </form>
    </body><html>
    """.format("is")


@app.route("/greet")
def greet():
    fname = request.args.get('fname', 'Mark Jigger Masacupan')
    char = request.args['char']
    fixedword = ('is')

    if fname == '' and char == '':
        msg = 'You did not tell your name and characteristic'
    elif fname == '':
        msg = 'You did not tell your name but you are ' + char
    elif char == '':
        msg = 'Your name ' + fixedword + ' ' + fname + \
            ' but you did not mention your characteristic'
    else:
        msg = 'Your name ' + fixedword + ' ' + fname + ' and you are ' + char

    return """
        <html><body>
            <h2>Hello {0}!</h2>
            {1}
      </body></html>
      """.format(fname, msg)


# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)
