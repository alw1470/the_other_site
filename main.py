from jinja2 import Environment, FileSystemLoader, select_autoescape
from flask import Flask, request, jsonify
from imagenes import url




env = Environment(
    loader=FileSystemLoader('template')

)
title = 'A TITLE'
name = 'KAOS'
elements = ['alberto', 'silvia','gonzalo']
titulo_producto = ['manzana', 'pera', 'piña']

template = env.get_template('index.html')
producto = env.get_template('producto.html')
my_html = template.render(title=title, name='KAOS', elements=elements, urls=url)
plantilla_producto = producto.render(title=title, name='KAOS', elements=elements, titulo_producto=titulo_producto)




app = Flask(__name__)

@app.route('/users', methods=['GET'])
def hello_world():

    if request.method == 'GET':
        return my_html

@app.route('/blog/<titulo_producto>')
def hello(titulo_producto):
    return plantilla_producto

if __name__ == "__main__":
    app.run() 