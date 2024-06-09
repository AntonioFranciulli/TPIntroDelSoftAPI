from flask import Flask, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

def set_connection():

    engine = create_engine("mysql+mysqlconnector://root@localhost/database")

    connection = engine.connect()
    return connection

def show_records(connection):
    query = "SELECT * FROM refugios"
    try:
        result = connection.execute(text(query))
        connection.commit()
    except SQLAlchemy as err:
        print("error",str(err.__cause__))
        

@app.route("/")
def home():
    return "Ruta creada"

@app.route("/crear_voluntario" , methods = ['GET'])
def crear_voluntario():
    conn = set_connection()
    site = show_records(conn)
    data= []
    for row in site:
        result = {}


#@app.route("/agregar_voluntario/<cuil>") , methods=['POST']


#@app.route("/...") , methods=['GET']"""

#@app.route("/eliminar_refugio/id_refugio") , methods=['DELETE']

@app.route("/eliminar_voluntario/<cuil>", methods=['DELETE'])
def eliminar_voluntario(cuil):
    conn = set_connection()
    query = f"DELETE FROM voluntarios WHERE cuil_voluntario = {cuil};"
    validation_query = f"SELECT FROM voluntarios WHERE cuil_voluntario = {cuil}"
    try:
        result = conn.execute(text(validation_query))
        if result.rowcount != 0:
            conn.execute(text(query))
            # el commit no se si es necesario, depende de como trabajemos sobre la base de datos
            # en pythonanywhere tiene autocommit asi que si lo usas te tira error 500
            conn.commit()
            conn.close()
            return jsonify({'message' : 'voluntario eliminado exitosamente'})
        else:
            conn.close()
            return jsonify({'message' : 'cuil inexistente'})
    except SQLAlchemyError as err:
            return jsonify({'message' : 'Se ha producido un error' + str(err.__cause__)})

if __name__ == '__main__': 
   app.run("127.0.0.1",port = "5050", debug = True)