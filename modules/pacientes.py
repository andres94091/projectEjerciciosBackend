from flask import Blueprint, Flask, request, jsonify
from models import db
from models.pacientes import getPacientes as modelGetPacientes
from models.pacientes import getListPaciente as modelGetPacientesLista
from models.pacientes import createPatient
from models.pacientes import deletePatientDocument
from models.pacientes import editarPaciente as modelEditarPaciente

bp = Blueprint('pacientes', __name__, url_prefix='/pacientes')


@bp.route('/', methods=['GET'])
def list():
    print(db.get_connection())
    return {'message': 'Este es el servicio que lista de pacientes'}, 200


@bp.route('/pacientes', methods=['GET'])
def getPacientes():
    return modelGetPacientes()


@bp.route('/pacientes_lista', methods=['GET'])
def getPacientesLista():
    respuesta = modelGetPacientesLista()
    return respuesta, respuesta.status


@bp.route('/crear_paciente', methods=['POST'])

# {
# 	"nombre": "Andres Felipe Castro Londoño",
# 	"edad": 25,
# 	"genero": 1,
# 	"numero_contacto": "1234567",
# 	"documento": "123456789"
# }

def createNewPatient():
    data = request.get_json()
    respuesta = createPatient(data)
    print(respuesta)
    return respuesta, respuesta.status


@bp.route('/eliminar_paciente_documento', methods=['DELETE'])
# {
# 	"documento": "987654321"
# }
def deletePatientDocumento():
    data = request.get_json()
    respuesta = deletePatientDocument(data['documento'])
    print(respuesta)
    return respuesta, respuesta.status

@bp.route('/editar_paciente', methods=['PUT'])
# {
# 	"documento": "123456789",
# 	"data": {
# 		"edad": 23
# 	}
# }
def editarPaciente():
    data = request.get_json()
    respuesta = modelEditarPaciente(data)
    print(respuesta)
    return respuesta, respuesta.status
