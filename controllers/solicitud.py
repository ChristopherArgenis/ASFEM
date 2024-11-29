from flask import Blueprint,  request, render_template, redirect
from services.filtrar_solicitud import filtro_solicitud
from link.link_db import Password
from services.conexion import Conector

Solicitud = Blueprint("solicitud", __name__)

pass_word = Password()
access = Conector(pass_word)
Solicitud.db = access.conectar().Almacen

@Solicitud.route('/Solicitud', methods=["GET", "POST"])
def solicitacion():
    if request.method == "POST":
        tratamiento = request.form.get("tratamientos")
        costo = request.form.get("costo")
        fecha = request.form.get("fecha")
        T_Previos = request.form.get("TratamientosPrevios")
        seguro_Medico = request.form.get("seguroMedico")
        padre = request.form.get("padre")
        madre = request.form.get("madre")
        hermanos = request.form.get("hermanos")
        otros = request.form.get("otros")
        ninguno = request.form.get("ninguno")

        list_data = [tratamiento, costo, fecha, T_Previos, seguro_Medico, [padre, madre, hermanos, otros, ninguno]]

        filtro = filtro_solicitud(list_data)
        result = filtro.filtrador()
        solicitud = filtro.get_solicitud()
        no_familiar = filtro.no_familiares()

        parametros = {"Tratamiento": solicitud.tratamiento,
                      "Costo": solicitud.costo,
                      "Fecha": solicitud.fecha,
                      "No. Tratamiento Previos": solicitud.t_previos,
                      "Seguro": solicitud.seguro_Medico,
                      "No. Familiares Lab": no_familiar}
        Solicitud.db.Solicitudes.insert_one(parametros)
        if result == True:
            return redirect('/Aceptado')
        elif result == False:
            return redirect('/Rechazado')
    return render_template("2_solicitud.html")