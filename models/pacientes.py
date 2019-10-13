from models import db
from flask import Flask, request, jsonify
from bson.json_util import dumps


def getPacientes():
    con = db.get_connection()
    dbejercicios = con.ModeloEjercicios
    try:
        pacientes = dbejercicios.pacientes
        retorno = dumps(pacientes.find({}))
        return jsonify(retorno)
    finally:
        con.close()
        print('coneccion cerrada')


def getListPaciente(parametro='documento'):
    con = db.get_connection()
    dbejercicios = con.ModeloEjercicios

    try:
        pacientes = dbejercicios.pacientes
        retorno = list(pacientes.find({}))
        lista = [d[parametro] for d in retorno]
        return jsonify({'data': lista, 'status': 200})
    finally:
        con.close()
        print('coneccion cerrada')


def createPatient(data):
    con = db.get_connection()
    dbejercicios = con.ModeloEjercicios

    try:
        pacientes = dbejercicios.pacientes
        pacientes.insert(data)
        return jsonify({'message': 'paciente insertado', 'status': 200})
    except:
        return jsonify({'message': 'fallo en la insercion', 'status': 500})
    finally:
        con.close()
        print('coneccion cerrada')

def deletePatientDocument(documento):
    con = db.get_connection()
    dbejercicios = con.ModeloEjercicios

    try:
        pacientes = dbejercicios.pacientes
        pacientes.delete_many({'documento': documento})
        return jsonify({'message': 'paciente eliminado', 'status': 200})
    except:
        return jsonify({'message': 'fallo al eliminar paciente', 'status': 500})

    finally:
        con.close()
        print('coneccion cerrada')

def editarPaciente(data):

    con = db.get_connection()
    dbejercicios = con.ModeloEjercicios

    try:
        pacientes = dbejercicios.pacientes
        print(data['data'])
        pacientes.find_one_and_update({'documento': data['documento']}, {'$set': data['data']})
        return jsonify({'message': 'paciente editado', 'status': 200})
    except:
        return jsonify({'message': 'fallo al editar un paciente', 'status': 500})

    finally:
        con.close()
        print('coneccion cerrada')