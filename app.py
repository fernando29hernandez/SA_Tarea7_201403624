# app.py
# import flask
from flask import Flask
## creacion de la app
app = Flask(__name__)
# funcion saludo
@app.route('/')
def hello_world():
    return 'Hello world!'

#funcion prueba de despliegue
@app.route('/despliegue')
def funcion2():
    return 'Funciono despliegue'

#funcion de prueba final
@app.route('/demo')
def funcion3():
    return 'Demostracion de despligue en aplicacion'

if __name__ == '__main__':
    #run server en el puerto 5000
    app.run(host='0.0.0.0')
