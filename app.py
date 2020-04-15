# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/despliegue')
def funcion2():
    return 'Funciono despliegue'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
