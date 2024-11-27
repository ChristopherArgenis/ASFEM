from flask import Blueprint, render_template, request
from pymongo import MongoClient

# Define un nuevo Blueprint con el nombre: 'database'
Database = Blueprint('database', __name__)

# Conexion a la Base de Datos
# conexion = MongoClient("mongodb+srv://christopherpreciadosilva:Y4cs6WRIUcDb90Eq@solicitudes.7r9rd.mongodb.net/")
conexion = MongoClient("mongodb+srv://christopherpreciadosilva:Y4cs6WRIUcDb90Eq@solicitudes.7r9rd.mongodb.net/?retryWrites=true&w=majority&appName=Solicitudes")

# Conexion de la Aplicacion a la Base de Datos
Database.db = conexion.Almacen

# Iterar en los JSON de la Coleccion.
names = [name for name in Database.db.Solicitudes.find({})]

@Database.route('/pruebas', methods=["GET", "POST"])
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
        Database.db.Solicitudes.insert_one(parametros)
    return render_template("z_pruebas.html", nombres=names)