from flask import Flask, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from flask_cors import CORS
import requests
import json
import lib

app = Flask(__name__)
CORS(app, resources={r'*': {'origins': 'http://127.0.0.1:5000'}})

def set_connection():
    engine = create_engine("mysql+mysqlconnector://root@localhost/CalleSolidaria")
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

@app.route('/obtener_refugios_geojson', methods=['GET'])
def obtener_refugios():
    conn = set_connection()
    query = "SELECT * FROM refugios;"
    
    try:
        resultado = conn.execute(text(query))
    except SQLAlchemyError as err:
        conn.close() 
        return jsonify({"Error":"Se produjo un error al intentar procesar la solicitud pedida"}), 500
    #Abajo se plantea la estructura del geojson. La clave features tiene como valor asociado una lista vacia en la cual se iran guardando los puntos
    #a lo largo de la ejecucion de la función. 
    geojson_refugios = {
        "type": "FeatureCollection",
        "features": []
    }
    for fila in resultado: # aca lo que hago es recorrer cada refugio de la base de datos y guardar sus atributos en un diccionario llamado refugio
        refugio = {
            'id_refugio': fila.id_refugio,
            'nombre_refugio': fila.nombre_refugio,
            'direccion': fila.direccion,
            'descripcion': fila.descripcion,
            'tipo_refugio': fila.tipo_refugio,
            'telefono': fila.telefono,
            'lista_voluntarios': fila.lista_voluntarios
        }
        
        # Obtengo las coordenadas segun la direccion proporcionada a traves de la api. 
        TOKEN_ACCESO_A_API = 'pk.eyJ1IjoiYW50b25pb2ZyYW5jaXVsbGkiLCJhIjoiY2x4N3J4a2p5MHd2ajJycG1sZmU2ZWZvcSJ9.0hdKusxNrisOijQEdlLSrg'

        url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{refugio['direccion']}.json?access_token={TOKEN_ACCESO_A_API}"
        response = requests.get(url)
        data = response.json() # esto devuelve un objeto JSON proporcionado por la api de mapbox al hacer nuestra consulta de las coordenadas

        # aca abajo lo que se hace es comprobar que la clave features se encuentre en ese objeto json guardado en la variable data y ademas
        # tambien se evalua si tiene al menos un elemento significando que la api encontro una ubicacion para el refugio. 
        if 'features' in data and len(data['features']) > 0:
            coordinates = data['features'][0]['geometry']['coordinates'] # se guardan las coordenadas
        else:
            return jsonify({"error":"No se pudo encontrar las coordenadas de la direccion del refugio"}), 404
        #aca planteo la estructura particular del refugio con sus valores para luego insertarlo en la feature collection.
        geo = {
            "type": "Feature",
            "properties": {
                "description": refugio['descripcion'],
                "marker-symbol": "",
                "title": refugio['nombre_refugio'],
                "address": refugio['direccion'],

                #el resto de atributos que estan aca comentados se podrian incluir pero se debe integrarlos tambien en la estructura de la vista del mapa
                #"telefono": refugio['telefono'],
                #"tipo_refugio": refugio['tipo_refugio'],
                #"lista_voluntarios": refugio['lista_voluntarios']

            },
            "geometry": {
                "type": "Point",
                "coordinates": coordinates
            }
        }
        geojson_refugios["features"].append(geo)  #agrego a la lista de features el punto del refugio estructurado en este formato.
    
    conn.close()
    return jsonify(geojson_refugios), 200

@app.route("/obtener_refugios", methods=['GET'])
def mostrar_refugios():
    conn = set_connection()
    query = "SELECT * FROM refugios;"
    try:
        result = conn.execute(text(query))
        conn.close()
    except SQLAlchemyError as err:
        return jsonify({'message' : 'Se ha producido un error' + str(err.__cause__)}), 500
    data = []
    for row in result:
        entity={}
        entity['id']=row.id_refugio
        entity['nombre']=row.nombre_refugio
        entity['descripcion']=row.descripcion
        entity['direccion']=row.direccion
        entity['telefono']=row.telefono
        entity['tipo']=row.tipo_refugio
        entity['foto']=row.link_foto
        entity['voluntarios']=row.lista_voluntarios
        data.append(entity)
    return jsonify(data), 200

@app.route("/obtener_refugio/<id>", methods=['GET'])
def mostrar_refugio(id):
    conn = set_connection()

    POSICION_LISTA_VOL = 7
    lista_voluntarios = []
    seleccionar_refugio = f"SELECT * FROM refugios WHERE id_refugio={id};"
    try:
        refugio = conn.execute(text(seleccionar_refugio)).fetchone()
        if not refugio:
            return jsonify({ 'message': 'No se encontro un refugio con ese id' })
        
        if not refugio[POSICION_LISTA_VOL]: #Si no hay voluntarios crea listas vacias
            cuils_voluntarios = []
            lista_voluntarios = []
        else: #Si hay voluntarios lo convierte a lista
            cuils_voluntarios = json.loads(refugio[POSICION_LISTA_VOL])
        if len(cuils_voluntarios) == 1: # SEsto es cuando hay un voluntario
            seleccionar_voluntarios = f"SELECT * FROM voluntarios WHERE cuil_voluntario = {cuils_voluntarios[0]}"
            lista_voluntarios = conn.execute(text(seleccionar_voluntarios)).fetchall()
        elif len(cuils_voluntarios) > 1: #Esto cuando hay muchos voluntarios
            seleccionar_voluntarios = f"SELECT * FROM voluntarios WHERE cuil_voluntario IN {tuple(cuils_voluntarios)}" 
            lista_voluntarios = conn.execute(text(seleccionar_voluntarios)).fetchall()
        conn.close()
    except SQLAlchemyError as err:
        return jsonify({'message' : 'Se ha producido un error' + str(err.__cause__)}), 500
    
    voluntarios = [] #Voluntarios datos completos
    for vol in lista_voluntarios:
        voluntarios.append(tuple(vol[:5])) #Excluye el token

    data = {
        'id_refugio': refugio[0],
        'nombre_refugio': refugio[1],
        'direccion': refugio[2],
        'descripcion': refugio[3],
        'tipo_refugio': refugio[4],
        'telefono': refugio[5],
        'link_foto': refugio[6],
        # 'lista_voluntarios': voluntarios
    }
    return jsonify({ 'data_refugio': data, 'voluntarios': voluntarios}), 200

@app.route('/crear_refugio', methods = ['POST'])
def crearRefugio():
    conn= set_connection()
    newShelter = request.get_json()
    query = text("""INSERT INTO refugios(nombre_refugio, direccion, descripcion, tipo_refugio, telefono, link_foto)
    VALUES (:nombre_refugio, :direccion, :descripcion, :tipo_refugio, :telefono, :link_foto)
            """)
    try:
        conn.execute(query, {
        'nombre_refugio': newShelter["nombre_refugio"],
        'direccion': newShelter["direccion"],
        'descripcion': newShelter["descripcion"],
        'tipo_refugio': newShelter["tipo_refugio"],
        'telefono': newShelter["telefono"],
        'link_foto': newShelter["link_foto"]
    })
        conn.commit()
    except SQLAlchemyError as err:
        print("error",err.__cause__)
        return jsonify({'message': 'Se ha producido un error: ' + str(err)}), 500
    return jsonify({'message': 'Se ha agregado correctamente'}), 201

@app.route("/crear_voluntario", methods=['POST'])
def crear_voluntario():
    conn = set_connection() #Set connection to db
    volunteer = request.get_json() #Diccionario body

    ID_REFUGIO = 0 #Posiciones en la lista devuelta x la DB
    LISTA_VOLUNTARIOS = 7

    seleccionar_refugio = text("""SELECT * FROM refugios WHERE nombre_refugio = :nombre_refugio;""") #Obtiene refugio con nombre especifico

    insertar_voluntario = text("""INSERT INTO voluntarios(cuil_voluntario, puesto, telefono, nombre, id_refugio, link_foto)
    VALUES (:cuil_voluntario, :puesto, :telefono, :nombre, :id_refugio, :link_foto)
    """) #Inserta el voluntario en la tabla VOLUNTARIOS    

    update_refugio = text(""" UPDATE refugios SET lista_voluntarios = :lista_voluntarios
                WHERE id_refugio = :id_refugio;
    """) #Updatea la LISTA_VOLUNTARIOS de la lista de voluntarios

    try:
        refugio = conn.execute(seleccionar_refugio,{
            'nombre_refugio': volunteer["nombre_refugio"]
        }).fetchone() #Obtiene un refugio por nombre

        if not refugio:
            return jsonify({'message': 'No existe un refugio con ese nombre'}), 404

        conn.execute(insertar_voluntario, {
        'cuil_voluntario': volunteer["cuil_voluntario"],
        'puesto': volunteer["puesto"],
        'telefono': volunteer["telefono"],
        'nombre': volunteer["nombre"],
        'id_refugio': refugio[ID_REFUGIO],
        'link_foto': volunteer["link_foto"]
        }) #Los datos son los que se obtuvieron desde el body exceto el id que se obtuvo desde el refugio
        conn.commit() 

        if refugio[7] == None: #Si no habia un voluntario antes se crea una lista
            lista_voluntarios = [volunteer["cuil_voluntario"]]
        else: 
            lista_voluntarios = json.loads(refugio[LISTA_VOLUNTARIOS]) #Convierte "[]" => []
            lista_voluntarios.append(volunteer["cuil_voluntario"])

        lista_voluntarios = json.dumps(lista_voluntarios) #Convierte [] => "[]"
        

        conn.execute(update_refugio,{'id_refugio': refugio[ID_REFUGIO],'lista_voluntarios': lista_voluntarios})
        conn.commit()

    except SQLAlchemyError as err:
        print("error",err._cause_)
        return jsonify({'message': 'Se ha producido un error: ' + str(err)}), 500
    
    return jsonify({'message': 'Se ha agregado correctamente'}), 201

@app.route("/obtener_voluntario/<cuil>", methods=['GET'])
def obtener_voluntario(cuil: str):
    if not cuil.isdigit():
        return jsonify({ 'message': 'El cuil no es valido' }), 500
    POSICION_ID_REFUGIO = 4
    conn = set_connection()

    seleccionar_voluntario = f"SELECT * FROM voluntarios WHERE cuil_voluntario = {cuil};"
    seleccionar_refugio = f"SELECT nombre_refugio FROM refugios WHERE id_refugio = :id_refugio;"

    try:
        voluntario = conn.execute(text(seleccionar_voluntario)).fetchone() #Obtiene un refugio por nombre
        print(voluntario)
        if not voluntario:
            return jsonify({'message': 'No existe un voluntario con ese cuil'}), 404
        
        refugio = conn.execute(text(seleccionar_refugio), { 'id_refugio': voluntario[POSICION_ID_REFUGIO] }).fetchone()
        
        datos = {
        'cuil_voluntario': cuil,
        'puesto': voluntario[1],
        'telefono': voluntario[2],
        'nombre': voluntario[3],
        'id_refugio': voluntario[4],
        'nombre_refugio': refugio[0],
        'link_foto':voluntario[5]
        }

        return jsonify({ 'data': datos }), 200 #Excluyo el token
        
    except SQLAlchemyError as err:
        print("error",err._cause_)
        return jsonify({'message': 'Se ha producido un error: ' + str(err)}), 500

@app.route("/eliminar_refugio/<id>", methods=['DELETE'])
def eliminar_refugio(id):
    conn = set_connection()  
    query = "DELETE FROM refugios WHERE id_refugio = :id;"
    query_validation = "SELECT * FROM refugios WHERE id_refugio = :id;"
    try:
        val_result = conn.execute(text(query_validation), {"id": id})
        if val_result.rowcount!= 0:
            conn.execute(text(query), {"id": id})
            conn.commit()
            conn.close()
            return jsonify({'message': 'Refugio eliminado exitosamente'})
        else:
            conn.close()
            return jsonify({'message': 'id inexistente'}), 404
    except SQLAlchemyError as err:
        conn.close()
        return jsonify({'message': 'Se ha producido un error: ' + str(err)}), 500
    finally:
        conn.close()

    return jsonify({'message': 'se ha eliminado correctamente'}), 200

@app.route("/eliminar_voluntario/<cuil>", methods=['DELETE'])
def eliminar_voluntario(cuil: str):
    if not cuil.isdigit(): return jsonify({ 'message': 'El cuil es invalido' })

    conn = set_connection()

    update_refugio = text(""" UPDATE refugios SET lista_voluntarios = :lista_voluntarios
        WHERE id_refugio = :id_refugio;
    """) #Updatea la LISTA_VOLUNTARIOS de la lista de voluntarios
    seleccionar_voluntario = text(f"SELECT * FROM voluntarios WHERE cuil_voluntario = {cuil}") #Selecciona voluntario mediante cuil
    seleccionar_refugio = text("""SELECT * FROM refugios WHERE id_refugio = :id_refugio;""") #Selecciona refugio mediante id
    eliminar_voluntario = f"DELETE FROM voluntarios WHERE cuil_voluntario = {cuil};" #Elimina voluntario por cuil
    POSICION_ID_REFUGIO = 4 
    POSICION_LISTA_VOLUNTARIOS = 7

    try:
        voluntario = conn.execute(seleccionar_voluntario).fetchone() #busco voluntario
        if not voluntario:
            return jsonify({'message' : 'cuil inexistente'})
        
        refugio = conn.execute(seleccionar_refugio, { 'id_refugio': voluntario[POSICION_ID_REFUGIO]}).fetchone() #busco refugio
        
        if not refugio:
            return jsonify({'message' : 'Ese voluntario no esta inscripto en ningun refugio valido'})
        
        lista_vol = json.loads(refugio[POSICION_LISTA_VOLUNTARIOS])
        lista_vol_actualizada = lib.aux_eliminar_voluntario(lista_vol, int(cuil)) #Elimino voluntario de lista voluntario

        conn.execute(update_refugio,{'id_refugio': voluntario[POSICION_ID_REFUGIO],'lista_voluntarios': lista_vol_actualizada}) #Update lista_vol en refugio
        conn.commit()

        #Ahora se elimina el voluntario de la TABLA DE VOLUNTARIOS
        result = conn.execute(text(eliminar_voluntario))
        if result.rowcount != 0:
            conn.execute(text(eliminar_voluntario))
            # el commit no se si es necesario, depende de como trabajemos sobre la base de datos
            # en pythonanywhere tiene autocommit asi que si lo usas te tira error 500
            conn.commit()
            conn.close()
            return jsonify({'message' : 'Voluntario eliminado exitosamente'})
        else:
            conn.close()
            return jsonify({'message' : 'Cuil inexistente'})
    except SQLAlchemyError as err:
            return jsonify({'message' : 'Se ha producido un error' + str(err.__cause__)})
    
#acá probé que los refugios se eliminen en base al id luego de hacer el get refugios, no sé cómo vamos a implementar el tema del token para que solamente los que crearon los refugios puedan modificarlo
@app.route('/refugios/<id>',methods = ['PATCH'])
def modificar_usuario(id):
    conn = set_connection()
    mod_refugio = request.get_json()
    #acá los datos tienen que ser mandados por el body
    query = query = f""" UPDATE refugios SET nombre_refugio = '{mod_refugio["nombre_refugio"]}'
            {f", direccion = '{mod_refugio['direccion']}'"}
            {f",descripcion = '{mod_refugio['descripcion']}'"}
            {f",telefono = '{mod_refugio['telefono']}'"}
            {f",link_foto = '{mod_refugio['link_foto']}'"}
            WHERE id_refugio = {id};
            """

    query_validation = f"SELECT * FROM refugios WHERE id_refugio = {id};"
    try:
        val_result = conn.execute(text(query_validation))
        if val_result.rowcount != 0:
            result = conn.execute(text(query))
            conn.commit()
            conn.close()
            return jsonify({'message':'se ha modificado correctamente' + query}),200
        else:
            conn.close()
            return jsonify({'message': 'El refugio buscado no existe'}),404
    except SQLAlchemyError as err:
            return jsonify({'message': f'Error al modificar el refugio: {err}'}), 500

#probablemente algo tengamos que modificar de este, porque deberiamos ver cómo hacer para que no cualquiera pueda modificar la base de datos.

@app.route('/modificar_voluntario/<cuil>', methods=['PATCH'])
def modificar_voluntario(cuil):
    conn = set_connection()
    mod_vol = request.get_json()
    print(mod_vol)
    query_id_refugio = 'SELECT id_refugio FROM refugios WHERE nombre_refugio = :nombre_refugio'
    id_refugio = conn.execute(text(query_id_refugio), { 'nombre_refugio': mod_vol['nombre_refugio'] }).fetchone()
    # Los datos se tienen que mandar por el body del request
    #No estoy seguro que sea buena práctica poder modificar el cuil si lo usamos como PK. Por las dudas lo dejo por ahora
    editar_voluntario = f"""UPDATE voluntarios SET 
                nombre = '{mod_vol['nombre']}',
                puesto = '{mod_vol['puesto']}',
                telefono = '{mod_vol['telefono']}',
                id_refugio = '{id_refugio[0]}',
                link_foto = '{mod_vol['foto']}' WHERE cuil_voluntario = :cuil AND token=:token"""
    

    query_validation = f"SELECT * FROM voluntarios WHERE cuil_voluntario = :cuil AND token=:token"
    try:
        val_result = conn.execute(text(query_validation), { 'token': mod_vol['token'], 'cuil': mod_vol['cuil_voluntario'] })
        if val_result.rowcount != 0:
            conn.execute(text(editar_voluntario), { 'token': mod_vol['token'], 'cuil': mod_vol['cuil_voluntario'] })
            conn.commit()
            conn.close()
        else:
            conn.close()
            return jsonify({'message': "El voluntario no existe"}), 404
    except SQLAlchemyError as err:
        return jsonify({'message': str(err.__cause__)}), 500
    return jsonify({'message': 'Se ha modificado correctamente'}), 200