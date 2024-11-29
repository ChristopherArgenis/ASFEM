class Solicitud:
    def __init__(self, tratamiento, costo, fecha, t_previos, seguro_Medico, ingreso_f):
        self.comprobado = None
        self.tratamiento = tratamiento
        self.costo = costo
        self.fecha = fecha
        self.t_previos = t_previos
        self.seguro_Medico = seguro_Medico
        self.ingreso_f = ingreso_f