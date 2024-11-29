from models.solicitud import Solicitud

class filtro_solicitud:
    def __init__(self, ld):
        self.solicitud = Solicitud(ld[0], int(ld[1]), ld[2], int(ld[3]), ld[4], ld[5])
        self.puntaje = 0
        
    def filtrador(self):
        if self.solicitud.tratamiento == "Quirúrgicos":
            self.puntaje += 2
        elif self.solicitud.tratamiento != "Quirúrgicos":
            self.puntaje += 1

        if self.solicitud.costo < 2000:
            self.puntaje += 1
        else:
            self.puntaje += 0

        if self.solicitud.t_previos == 1:
            self.puntaje += 2
        elif self.solicitud.t_previos == 0:
            self.puntaje += 1

        if self.solicitud.seguro_Medico == "No":
            self.puntaje += 2
        elif self.solicitud.seguro_Medico == "Seguro Facultativo":
            self.puntaje += 1
        else:
            self.puntaje += 0

        if self.solicitud.ingreso_f:
            for familiar in self.solicitud.ingreso_f:
                if familiar == None:
                    self.solicitud.ingreso_f.remove(familiar)
            if len(self.solicitud.ingreso_f) == 1:
                self.puntaje += 2
            elif len(self.solicitud.ingreso_f) == 2:
                self.puntaje += 1
            elif len(self.solicitud.ingreso_f) == 3:
                self.puntaje += 0

        if self.puntaje > 4:
            self.solicitud.comprobado = "Aceptado"
            return True
        else:
            self.solicitud.comprobado = "Rechazado"
            return False
        
    def get_solicitud(self):
        return self.solicitud
    
    def no_familiares(self):
        for familiar in self.solicitud.ingreso_f:
            if familiar == None:
                    self.solicitud.ingreso_f.remove(familiar)
        return len(self.solicitud.ingreso_f)