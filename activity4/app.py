from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('./index.html')


# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)
# What a Crap! Zeet via AWS, may bayad ang deployment w/c 13 hours per 1 dollar sa Debit Card ko, shuta.
# app.run(host='0.0.0.0', port=5000)
# https://afdr2rblr6.execute-api.us-east-2.amazonaws.com/
