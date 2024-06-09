from flask import Flask, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
engine = create_engine("mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}")#cambiar url para conectar a su base de datos local

@app.route("/")
def home():
    return "OK"

@app.route("/eliminar_voluntario/<cuil>", methods=['DELETE'])
def eliminar_voluntario(cuil):
    conn = engine.connect()
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