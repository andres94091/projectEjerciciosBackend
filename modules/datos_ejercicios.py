from flask import Blueprint
from models import db

bp = Blueprint('datos_capturas', __name__, url_prefix='/datos_capturas')

@bp.route('/', methods=['GET'])
def list():
    print(db.get_connection())
    return "Este es el servicio que lista de datos de ejercicios"