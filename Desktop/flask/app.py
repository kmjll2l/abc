from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/test1')
def abc():
    return '<h1>안녕하세요</h1><input type = "textbox"/>'

if __name__ == '__main__':
    app.run(host='192.168.56.1', port='8888', debug=True)