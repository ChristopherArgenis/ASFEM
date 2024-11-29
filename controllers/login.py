from flask import Blueprint, request, render_template, redirect
from link.link_db import Password
from services.conexion import Conector

Login = Blueprint("login", __name__)

pass_word = Password()
access = Conector(pass_word)
Login.db = access.conectar().Almacen

@Login.route('/', methods=["GET", "POST"])
def login():
    mensaje = None
    matricula, correo = "", ""
    if request.method == "POST":
        # Capturar las entradas
        matricula = request.form.get("matricula")
        correo = request.form.get("correo_electronico")

        # Encontrar el registro de este estudiante
        try:
            if Login.db.Solicitudes.find({matricula: correo}):
                mensaje = None
                return redirect('/Solicitud')
        except:
            mensaje = "La matricula o el correo estan equivocados"
            return render_template("1_inicio_sesion.html", mensaje=mensaje)
    return render_template("1_inicio_sesion.html", mensaje=mensaje)