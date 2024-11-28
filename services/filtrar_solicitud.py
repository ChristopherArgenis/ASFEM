from models.solicitud import Solicitud

class filtro_solicitud:
    def __init__(self, list_data):
        self.solicitud = Solicitud(list_data[0])
        
    def filtrador(self):
        if self.solicitud.x == 1:
            self.solicitud.comprobado = "Aceptado"
            return True
        else:
            self.solicitud.comprobado = "Rechazado"
            return False