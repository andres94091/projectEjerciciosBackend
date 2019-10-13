from flask import Blueprint
from models import db

bp = Blueprint('ejercicios', __name__, url_prefix='/ejercicios')

@bp.route('/', methods=['GET'])
def list():
    print(db.get_connection())
    return "Este es el servicio que lista de pacientes"