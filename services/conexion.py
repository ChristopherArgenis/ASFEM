from pymongo import MongoClient

class Conector:
    def __init__(self, password):
        self.password = password

    def conectar(self):
        v_conector = MongoClient(self.password.get_pass())
        return v_conector