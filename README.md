# Tarea 7 - Software Avanzado - Primer Semestre 2020 
##  Proyecto en Docker-Compose con DevOps
Lenguajes Utilizados:
  - Python 2.7
  - python(flask)


## Archivos dockerfile y docker-compose.yml

### Dockerfile
```bash
FROM python:2.7
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python app.py
```

- FROM: imagen de la cual nos vamos a basas para este dockerfile.
- ADD: copia de una carpeta hacia una dentro de la imagen.
- WORKDIR: setea la carpeta como area de trabajo de la imagen.
- RUN: recibe un comando el cual ejecutara una vez para construir la imagen.
- CMD: comando final del dockerfile, en su mayoria sirve para habilitar o correr la aplicacion.
### docker-compose.yml
```bash
version: '2'
services:
    web:
        build: .
        ports:
            - "5000:5000"
        volumes:
            - .:/code
```

- "version ‘2’": Los archivos docker-compose.yml son versionados, lo que significa que es muy importante indicar la version de las instrucciones que queremos darle. A medida de que Docker evoluciona, habrá nuevas versiones, pero de todos modos, siempre hay compatabilidad hacia atras, al indicar la version de la receta.

- "build .": Se utiliza para indicar donde está el Dockerfile que queremos utilizar para crear el contenedor. Al definier “.” automaticamente considerará el Dockerfile existente en directorio actual.

- "ports":Esto permitirá que accediendo a IP:5000 podamos probar el sitio generador por flask.

- "volumes": Aqui hacemos que el directorio actual se mapee directamente con el /code, para que se utilice como carpeta persistente.

## Aplicacion en flask

```bash
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
```

## Poner en escucha el servicio

```bash 
'''run server en el puerto 5000'''
if __name__ == '__main__':
    app.run(port='5000')
```

## Scripy deploy.sh

Para correr esta aplicación se hace uso de un shell script el cual su contenido es el siguiente:
```bash 
#!/bin/sh
cd  SA_Tarea7_201403624
sudo git pull origin master
sudo docker-compose  up --build -d
```
# Video Demo
   [![Ver en youtube](https://img.youtube.com/vi/u4S9xrW2Je0/0.jpg)](https://youtu.be/u4S9xrW2Je0)
