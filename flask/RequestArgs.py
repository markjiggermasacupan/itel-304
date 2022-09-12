from flask import Flask

from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    html><body>
      <h1>Hello, {0}!</h1>
          Time is {1}.
      </body></html>
      """.format(
          name, str(datetime.now()))
          
# Launch the Flask dev server
app.run(host="localhost", debug=True)


if __name__ == '__main__':
    app.run()
