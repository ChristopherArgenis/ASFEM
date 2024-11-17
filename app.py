from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
# Conexion a la Base de Datos
conexion = MongoClient("mongodb+srv://christopherpreciadosilva:Y4cs6WRIUcDb90Eq@solicitudes.7r9rd.mongodb.net/")

# Conexion de la Aplicacion a la Base de Datos
app.db = conexion.Almacen

# Iterar en los JSON de la Coleccion.
names = [name for name in app.db.Solicitudes.find({})]

@app.route('/')
def login():
    return "<h1> Inicio de Sesion </h1>"

@app.route('/Solicitud')
def form():
    return "<h1> Solicitud </h1>"

@app.route('/Comprobante')
def output():
    return ""

@app.route('/pruebas', methods=["GET", "POST"])
def test():
    name = ""
    if request.method == "POST":
        # Apartado de Adquisicion de Datos
        name = request.form.get("name")

        # Formato JSON (NoSQL)
        parametros = {"Nombre": name}

        # Agregar a la Pagina (Cambio Dinamico)
        names.append(parametros)

        # Agregar a la Base de Datos
        app.db.Solicitudes.insert_one(parametros)
    return render_template("z_pruebas.html", nombres=names)

if __name__ == '__main__':
    app.run()