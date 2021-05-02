from flask import Flask, render_template, abort
import json
app = Flask(__name__)

with open ("books.json") as f:
    datos = json.load(f)

@app.route('/', methods=["GET","POST"])
def inicio():
    return render_template("inicio.html", lista=datos)

app.run("0.0.0.0",5000,debug=True)