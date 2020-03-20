from flask import Blueprint, Flask, request, jsonify
from models.hashYear import hashBaseDatos, hashlog
bp = Blueprint('hashSeguridad', __name__, url_prefix='/login')

@bp.route('/', methods=['GET'])
def list():
    print(db.get_connection())
    return "Este es el servicio que lista de pacientes"

@bp.route('/idSeguridad', methods=['POST'])
def hashBaseDatosController():
    año = request.get_json()['año']
    idSeguridad = hashBaseDatos(año)
    return { "status": 200, "data": { "idSeguridad": idSeguridad }, "message": 'idSeguridad'}

@bp.route('/idLog', methods=['POST'])
def hashLogController():
    año = request.get_json()['año']
    idSeguridad = hashlog(año)
    return { "status": 200, "data": { "idSeguridad": idSeguridad }, "message": 'idSeguridad'}