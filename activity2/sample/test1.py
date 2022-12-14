from flask import Flask, request, WSGIServer

from datetime import datetime

app = Flask(__name__)

http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()


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
        msg = """
        <html><body>
            <p>
                How can I know you, if you do not tell your name?
                <a href="http://127.0.0.1:5000/">Go back!</a>
            </p>
        </body></html>"""

    else:
        """
        <html><body>
            <p>
                Your full name {0}, fname + and your characteristic {0} + char
            </p>
        </body></html>
    """.format("is")

    return """
        <html><body>
            <h2>Hello {0}!</h2>
            {1}
      </body></html>
      """.format(fname, msg, "is")


# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)


# if __name__ == '__main__':
#    app.run()
