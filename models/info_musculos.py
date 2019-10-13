from models import db
from flask import Blueprint, Flask, request, jsonify
from bson.json_util import dumps

def getMusculos(documento):
    con = db.get_connection()
    dbejercicios = con.ModeloEjercicios
    try:
        musculos = dbejercicios.info_musculo
        retorno = dumps(musculos.find({"paciente.documento": documento}))
        return jsonify(retorno)
    finally:
        con.close()
        print('coneccion cerrada')

def getMusculosLista():
    con = db.get_connection()
    dbejercicios = con.ModeloEjercicios

    try:
        musculos = dbejercicios.musculos
        retorno = list(musculos.find({}))
        lista = [d['musculo'] for d in retorno]
        return jsonify({'data': lista, 'status': 200})
    finally:
        con.close()
        print('coneccion cerrada')

def guardarMusculoInfo(data):
    con = db.get_connection()
    dbejercicios = con.ModeloEjercicios
    try:
        musculosInfo = dbejercicios.info_musculo
        musculos = dbejercicios.musculos
        pacientes = dbejercicios.pacientes

        try:
            pacienteGuardar = list(pacientes.find({'documento': data['documento']}))
            musculoGuardar = list(musculos.find({'musculo': data['musculo']}))
            if (len(pacienteGuardar) == 1 and len(musculoGuardar) == 1 ):
                informacionGuardar = data['data']
                informacionGuardar['paciente'] = {'documento': pacienteGuardar[0]['documento'],
                                                  'id_documento': str(pacienteGuardar[0]['_id'])}
                informacionGuardar['musculo'] = {'nombre': musculoGuardar[0]['musculo'],
                                                  'id_nombre_musculo': str(musculoGuardar[0]['_id'])}

                print(informacionGuardar)

                musculosInfo.insert(informacionGuardar)
                return jsonify({'message': 'informacion muscular guardada', 'status': 200})
            elif (len(pacienteGuardar) != 1):
                return jsonify({'message': 'paciente no existe', 'status': 500})
            else:
                return jsonify({'message': 'musculo no existe', 'status': 500})

        except:
            return jsonify({'message': 'fallo en la insercion', 'status': 500})
    except:
        return jsonify({'message': 'fallo en la insercion', 'status': 500})
    finally:
        con.close()
        print('coneccion cerrada')

def guardarMusculo(data):
    con = db.get_connection()
    dbejercicios = con.ModeloEjercicios

    try:
        musculos = dbejercicios.musculos
        musculos.insert(data)
        return jsonify({'message': 'musculo insertado', 'status': 200})
    except:
        return jsonify({'message': 'fallo en la insercion', 'status': 500})
    finally:
        con.close()
        print('coneccion cerrada')






