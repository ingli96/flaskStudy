from flask import Flask

app = Flask(__name__)

lst = [1]

@app.route('/')
def massive():  # put application's code here
    lst.append(1)
    return "-".join(str(i) for i in lst)



@app.route('/abc/')
def abc():  # put application's code here
    return 'a-b-c'


if __name__ == '__main__':
    app.run()
