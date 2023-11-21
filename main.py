import cx_Oracle
from flask import Flask, render_template,request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)

oracle_user = 'rm552262'
oracle_password = '210804'
oracle_host = 'oracle.fiap.com.br'
oracle_port = '1521'
oracle_sid = 'orcl'

# conectando ao banco de dados
db_uri = f"oracle+cx_oracle://{oracle_user}:{oracle_password}@{oracle_host}:{oracle_port}/{oracle_sid}"
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
# Desativar rastreamento de modificações
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class T_SIP_USUARIO(db.model):
    __tablename__ = 'T_SIP_USUARIO'
    id_usuario = db.Column(db.Integer, primaryKey = True, autoincrement = True )
    id_usuario_endereco = db.Column(db.Integer, foreignKey = True, autoincrement = True)
    nm_completo = db.Column(db.String(250))
    idade = db.Column(db.Integer)
    email = db.Column(db.String(200))
    telefone = db.Column(db.String(9))
    nm_usuario = db.Column(db.String(100))
    senha = db.Column(db.Float)
    peso = db.Column(db.Float)
    genero = db.Column(db.String(75))
    data_nascimento = db.Column()



@app.route('/usuario')
def usuario():
    return 'ola'



if __name__ == "__main__":
    app.run(debug=True)