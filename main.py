from jinja2 import Environment, FileSystemLoader, select_autoescape
from flask import Flask, request, jsonify
from imagenes import url
from flask_bootstrap import Bootstrap
import json



env = Environment(
    loader=FileSystemLoader('template')

)
title = 'A TITLE'
name = 'KAOS'
elements = ['alberto', 'silvia','gonzalo']
titulo_producto = ['manzana', 'pera', 'piña']

template = env.get_template('index.html')
template_json = env.get_template('json.html')
my_html = template.render(title=title, name='KAOS', elements=elements, urls=url)






app = Flask(__name__)
bootstrap = Bootstrap(app)






@app.route('/home', methods=['GET'])
def hello_world():
    if request.method == 'GET':
        return my_html

@app.route('/', methods=['GET'])
def json_pruba():
    with open("corgis.json", "r") as f:
        corgis = json.load(f)
    json_html = template.render(imagen=imagen)
    if request.method == 'GET':
        return json_html
if __name__ == "__main__":
    app.run() 