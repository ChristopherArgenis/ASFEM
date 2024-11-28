from flask import Blueprint,  request, render_template, redirect
from services.filtrar_solicitud import filtro_solicitud

Solicitud = Blueprint("solicitud", __name__)

@Solicitud.route('/Solicitud', methods=["GET", "POST"])
def solicitacion():
    if request.method == "POST":
        x = request.form.get("x")
        x = int(x)
        list_data = [x]
        filtro = filtro_solicitud(list_data)
        result = filtro.filtrador()
        if result == True:
            return redirect('/Aceptado')
        elif result == False:
            return redirect('/Rechazado')
    return render_template("2_solicitud.html")