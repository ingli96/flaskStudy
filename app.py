from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/abc/')
def abc():  # put application's code here
    return 'a-b-c'


if __name__ == '__main__':
    app.run()
