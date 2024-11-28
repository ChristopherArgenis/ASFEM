from flask import Flask
from controllers.database import Database
from controllers.login import Login
from controllers.solicitud import Solicitud
from controllers.comprobante import Comprobante

app = Flask(__name__)
app.register_blueprint(Database)
app.register_blueprint(Login)
app.register_blueprint(Solicitud)
app.register_blueprint(Comprobante)

if __name__ == '__main__':
    app.run()