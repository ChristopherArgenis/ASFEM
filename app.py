from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return "<h1> Inicio de Sesion </h1>"

@app.route('/Solicitud')
def form():
    return "<h1> Solicitud </h1>"

@app.route('/Comprobante')
def output():
    return ""

@app.route('/pruebas')
def test():
    return render_template("z_pruebas.html")

if __name__ == '__main__':
    app.run()