from flask import Flask, request

from datetime import datetime

app = Flask(__name__)

@app.route('/user/<name>')
def greetings(name):
    name = request.args['name']
    fixed = request.args['fixed']
    return 'Hello ' + name + '!' + fixed

app.ad_url_rule('/hello', 'hello')


# Launch the Flask dev server
app.run(host="localhost", debug=True)
