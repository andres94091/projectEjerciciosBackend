from models import db


def listar():
    print(db.get_connection())
    print("Se listaron los aviones")

def eliminar(nombre):
    print("Se elimino un avion")
