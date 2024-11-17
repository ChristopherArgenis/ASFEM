from flask import Flask

app = Flask(__name__)

@app.route('/Iniciar Sesion')
def login():
    return "<h1> Inicio de Sesion </h1>"

@app.route('/Solicitud')
def form():
    return "<h1> Solicitud </h1>"

@app.route('/Comprobante')
def output():
    return ""

if __name__ == '__main__':
    app.run()