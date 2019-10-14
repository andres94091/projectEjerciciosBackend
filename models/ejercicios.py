from models import db
from flask import Blueprint, Flask, request, jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId

def getMusculos(documento):
    con = db.get_connection()
    dbejercicios = con.ModeloEjercicios
    try:
        pacientes = dbejercicios.pacientes
        datos_ejercio = dbejercicios.datos_ejercicio
        ejercicios = dbejercicios.ejercicios
        musculos = dbejercicios.musculos

        paciente = dict(pacientes.find_one({'documento': documento}))
        capturasPaciente = list(datos_ejercio.find({'paciente': str(paciente['_id'])}))
        respuesta = []
        if (len(capturasPaciente) > 0):
            for registro in capturasPaciente:
                ejercicioRealizado = ejercicios.find_one({'_id': ObjectId(registro['ejercicio'])})
                musculoRealizado = musculos.find_one({'_id': ObjectId(registro['musculo'])})

                del registro['ejercicio'], registro['musculo'], registro['paciente'], registro['_id']
                del ejercicioRealizado['_id'], musculoRealizado['_id']

                ejercicioDatos = {**registro , **ejercicioRealizado, **musculoRealizado}
                respuesta.append(ejercicioDatos)

            return {'message': 'ejercicios del paciente', 'status': 200, 'data': respuesta}
        else:
            return jsonify({'message': 'paciente no tiene registros en la base de datos', 'status': 404})
    finally:
        con.close()
        print('coneccion cerrada')