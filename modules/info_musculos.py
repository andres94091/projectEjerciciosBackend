from flask import Blueprint, Flask, request, jsonify
from models import db
from models.info_musculos import getMusculos as modelGetMusculos
from models.info_musculos import getListPaciente as modelGetPacientesLista

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
    respuesta = modelGetPacientesLista()
    return respuesta, respuesta.status