from flask import Flask, render_template, request
from controllers.database import Database

app = Flask(__name__)
app.register_blueprint(Database)

@app.route('/')
def login():
    return "<h1> Inicio de Sesion </h1>"

@app.route('/Solicitud')
def form():
    return "<h1> Solicitud </h1>"

@app.route('/Comprobante')
def output():
    return "<h1> Comprabantes </h1>"

if __name__ == '__main__':
    app.run()