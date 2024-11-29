class Password:
    def __init__(self):
        self._pass = "mongodb+srv://christopherpreciadosilva:Y4cs6WRIUcDb90Eq@solicitudes.7r9rd.mongodb.net/?retryWrites=true&w=majority&appName=Solicitudes"
        self._pass_compass = "mongodb+srv://christopherpreciadosilva:Y4cs6WRIUcDb90Eq@solicitudes.7r9rd.mongodb.net/"

    def get_pass(self):
        return self._pass
    
    def get_pass_compass(self):
        return self._pass_compass