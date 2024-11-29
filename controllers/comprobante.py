from flask import Blueprint, render_template, redirect, request

Comprobante = Blueprint("comprobante", __name__)

@Comprobante.route('/Aceptado', methods=["GET", "POST"])
def aceptacion():
    if request.method == "POST":
        return redirect('/')
    return render_template("Aceptado.html")

@Comprobante.route('/Rechazado', methods=["GET", "POST"])
def rechazar():
    if request.method == "POST":
        return redirect('/')
    return render_template("Rechazado.html")