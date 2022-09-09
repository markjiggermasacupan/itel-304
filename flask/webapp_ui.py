from flask import Flask

from datetime import datetime

app = Flask(__name__)


@app.route('/')

def home():
    return """
        <html><body>
              <h2>Welcome to the Greeter</h2>
              <form action="/greet">
                 What's your name? <input type='text' name='username'><br>
                 What's your favorite food? <input type='text' name='favfood'><br>
                 <input type='submit' value='Continue'>
              </form>
        </body></html>
        """

@app.route('/greet)
def greet():
    username = request.args.get('Username', 'World')
    favfood = request.args['favfood']
    if favfood == '':
        msg = 'You did not tell me your favorite food.'
    else:
        msg = 'I like ' + favfood + ', too."

    return """
      <html><body>
          <h2>Hello, {0}!</h2>
          {1}
      </body></html>
      """.format(username, msg)

# Launch the FlasyPy dev server
app.cun(host="localhost", debug=True)


if __name__ == '__main__':
    app.run()
