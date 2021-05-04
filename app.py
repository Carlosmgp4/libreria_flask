import os
from flask import Flask, render_template, abort
import json
app = Flask(__name__)

with open ("books.json") as f:
    datos = json.load(f)

@app.route('/', methods=["GET","POST"])
def inicio():
    return render_template("inicio.html", lista=datos)

@app.route('/<isbn>')
def detalles(isbn):
    for lib in datos:
        if lib.get("isbn")==isbn:
            num_autores = len(lib.get("authors"))
            num_categoria = len(lib.get("categories"))
            return render_template("detalles.html",libro=lib,num_autores=num_autores,num_categoria=num_categoria)
    abort(404)

@app.route('/categoria/<nomcate>')
def categoria(nomcate):
    lis=[]
    for ca in datos:
        if nomcate in ca.get("categories"):
            lis.append(ca.get("title"))

    return render_template("categoria.html",lis=lis,nom=nomcate)
                
port=os.environ["PORT"]
app.run("0.0.0.0", int(port) ,debug=False)