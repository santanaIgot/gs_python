import cx_Oracle
from flask import Flask, render_template,request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy, Date
from sqlalchemy import create_engine
import datetime

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
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario_endereco = db.Column(db.Integer, foreignKey = True, autoincrement = True)
    nm_completo = db.Column(db.String(250))
    email = db.Column(db.String(200))
    telefone = db.Column(db.String(9))
    nm_usuario = db.Column(db.String(100))
    senha = db.Column(db.Float)
    peso = db.Column(db.Float)
    genero = db.Column(db.String(75))
    data_nascimento = db.Column(Date)




@app.route('/usuario', methods = ['POST'])
def usuario():
    try:
     data = request.get_json()
     novo_usuario = T_SIP_USUARIO(
         nm_completo=data['nm_completo'],
         idade=data['idade'],
         email=data['email'],
         telefone=data['telefone'],
         nm_usuario=data['nm_usuario'],
         senha=data['senha'],
         peso=data['peso'],
         genero=data['genero'],
         data_nascimento=datetime.datetime.strptime(
             data['data_nascimento'], '%Y-%m-%d').date()
     )
     db.session.add(novo_usuario)
     db.session.commit()
     return jsonify({'message':'Usuario adicionado com sucesso'}),201
    except Exception as e:
        return jsonify({'error': f'Erro ao adicionar usuário: {str(e)}'}), 500

       
            









if __name__ == "__main__":
    app.run(debug=True)