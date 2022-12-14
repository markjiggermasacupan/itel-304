from flask import Flask, request

from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    return """
    <html><body>
        <h1>Hello, my name is, My charateristic is </h1>
    </body><html>""".format({})


@app.route("/greet")
def greet():
    username = request.args.get('username', 'World')
    favfood = request.args['favfood']
    if favfood == '':
        msg = 'You did not tell me your favorite food.'
    else:
        msg = 'I like + favfood + ', 'too.'
    return """
      <html><body>
        <h2>Hello, {0}!</h2>
      </body></html>
      """.format(username, msg)


# Launch the Flask dev server
app.run(host="localhost", debug=True)


# if __name__ == '__main__':
#    app.run()
