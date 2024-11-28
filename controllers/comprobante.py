from flask import Blueprint, render_template

Comprobante = Blueprint("comprobante", __name__)

@Comprobante.route('/Aceptado')
def aceptacion():
    return render_template("Aceptado.html")

@Comprobante.route('/Rechazado')
def rechazar():
    return render_template("Rechazado.html")