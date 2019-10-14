from flask import Blueprint, Flask, request, jsonify
from models import db
from models.ejercicios import getMusculos as modelGetMusculos

bp = Blueprint('ejercicios', __name__, url_prefix='/ejercicios')

@bp.route('/', methods=['GET'])
def list():
    print(db.get_connection())
    return "Este es el servicio que lista de pacientes"

@bp.route('/ejercicios', methods=['GET'])
def getMusculos():
    documento = request.args.get('documento')
    return modelGetMusculos(documento)