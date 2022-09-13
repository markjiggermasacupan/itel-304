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
    Click <a href="/engaging activities">here</a> for the proceedings.
    </body></html>
    """.format(str(datetime.now()))


@app.route('/Engaging Activities')
# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class NoUserAndChar(Error):
    """Raised when the input value is no Name and Characteristic"""
    pass


class NoUser(Error):
    """Raised when the input value is no input User"""
    pass


class NoChar(Error):
    """Raised when the input value is no input Characteristic"""
    pass


def home():
    while True:
        try:
            username = (input
                        ("""
                 <html><body>
                    <h2> Welcome Man!</h2>
                        <form action="/greet">
                             Your full name {0} <input type='text' name='username'><br>
                        </form>
                </body><html>
                """)).format(username, 'is')

            char = (input("""
                    <html><body>
                            <form action="/greet">
                                And your characteristic {0} <input type='text' name='characteristic'><br>
                                <input type='submit' value='Continue'>
                            </form>
                    </body><html>
                    """)).format(char, 'is')

            if username == '' and char == '':
                raise NoUserAndChar

            elif char == '':
                raise NoUser

            elif username == '':
                raise NoChar
            else:
                msg1 = """
                    <html><body>
                        <h2> Welcome Man!</h2>
                            <form action="/greet">
                                Your full name {0} <input type='text' name='username'><br>
                                And your characteristic {0} <input type='text' name='char'><br>
                            <input type='submit' value='Continue'>
                            </form>
                    </body><html>
                    """.format(username, char, msg1, "is")
            break
        except NoUserAndChar:
            print("""
                        <html><body>
                        <p>Invalid input, you do not input your Name and Characteristic</p>
                        Please try again, <a href="/Engaging Activities">click here</a>
                        </body></html>
                    """)
        except NoUser:
            print("""
                        <html><body>
                            <p>Invalid input, you do not input your characteristic</p>
                            Please try again, <a href="/Engaging Activities">click here</a>
                        </body></html>
                    """)
        except NoChar:
            print("""
                      <p>Invalid input, you do not input your username</p>
                        Please try again, <a href="/Engaging Activities">click here</a>
                        <html><body>
                        </body></html>
                    """)


@app.route("/greet")
def greet():
    fname = request.args.get('fname')
    characteristic = request.args['characteristic']
    fixedword2 = ('is')

    if fname == '' and characteristic == '':
        msg = 'My name ' + fixedword2 + fname + ' and I am ' + characteristic
    elif fname == '':
        msg = 'You do not input your Name but I am ' + characteristic
    elif characteristic == '':
        msg = 'My Name' + fixedword2 + fname + 'but you do not input your Characteristic'
    else:
        msg = fname + fixedword2 + characteristic

    return """
        <html><body>
            <h2>Hello {0}!</h2>
            <p> I'm {1} </p>
      </body></html>
      """.format(fname, characteristic, msg, fixedword2)


# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)
