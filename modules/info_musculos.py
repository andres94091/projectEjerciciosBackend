from flask import Blueprint, Flask, request, jsonify
from models import db
from models.info_musculos import getMusculos as modelGetMusculos
from models.info_musculos import getMusculosLista as modelGetMusculosLista
from models.info_musculos import guardarMusculoInfo
from models.info_musculos import guardarMusculo

bp = Blueprint('musculos', __name__, url_prefix='/musculos')

@bp.route('/', methods=['GET'])
def list():
    print(db.get_connection())
    return "Este es el servicio que informacion musculos"

@bp.route('/musculos', methods=['GET'])
def getMusculos():
    documento = request.args.get('documento')
    return modelGetMusculos(documento)

@bp.route('/musculos_lista', methods=['GET'])
def getMusculosLista():
    respuesta = modelGetMusculosLista()
    return respuesta, respuesta.status

@bp.route('/guardar_informacion_musculo', methods=['POST'])
def saveMusculoInfo():
    data = request.get_json()
    respuesta = guardarMusculoInfo(data)
    return respuesta, respuesta.status

@bp.route('/guardar_musculo', methods=['POST'])
def saveMusculo():
    data = request.get_json()
    respuesta = guardarMusculo(data)
    return respuesta, respuesta.status