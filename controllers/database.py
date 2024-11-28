from flask import Blueprint, render_template, request
from link.link_db import Password
from pymongo import MongoClient

# Define a new Blueprint named 'welcome'
Database = Blueprint('database', __name__)

password_db = Password()

# Conexion a la Base de Datos
# conexion = MongoClient(password_db.get_pass_compass())
conexion = MongoClient(password_db.get_pass())

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