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