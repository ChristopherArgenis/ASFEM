from flask import Blueprint, request, render_template, redirect

Login = Blueprint("login", __name__)

@Login.route('/', methods=["GET", "POST"])
def login():
    mensaje = None
    registros = { 376907: "christopher.preciado.silva@uabc.edu.mx" }
    matricula, correo = "", ""
    if request.method == "POST":
        # Capturar las entradas
        matricula = request.form.get("matricula")
        correo = request.form.get("correo")

        # Encontrar el registro de este estudiante
        try:
            if registros[int(matricula)] == correo:
                mensaje = None
                return redirect('/Solicitud')
        except:
            mensaje = "La matricula o el correo estan equivocados"
            return render_template("1_inicio_sesion.html", mensaje=mensaje)
    return render_template("1_inicio_sesion.html", mensaje=mensaje)