from flask import Flask
# from controllers.database import Database
from controllers.login import Login

app = Flask(__name__)
# app.register_blueprint(Database)
app.register_blueprint(Login)

@app.route('/Solicitud')
def form():
    return "<h1> Solicitud </h1>"

@app.route('/Comprobante')
def output():
    return "<h1> Comprabantes </h1>"

if __name__ == '__main__':
    app.run()