# -*- coding: utf-8 -*-
from datetime import datetime
import pytz
import bcrypt

def year(dat):
    '''
   funcion que a partir de una fecha devuelve el año

   input:
       date(int) - fecha en timestamp

   output:
       value(int) - año de la fecha ingresada en timestamp

   '''

    print('Entrando en funcion  --- obtenerAnonacimiento')

    zona_horaria = 'America/Bogota'  # zona horaria de Colombia
    tz = pytz.timezone(zona_horaria)

    # Se recibe la fecha en milisegundos y se pasa a formato ctime -> %a %b %d %H:%M:%S %Y
    cstr = datetime.fromtimestamp(dat / 1000, tz).ctime()
    # Se debe indicar el formato de fecha que tiene Csrt
    cstr_formato = datetime.strptime(cstr, '%a %b %d %H:%M:%S %Y')
    # Se cambia el formato teniendo en cuenta el formato anterior en este caso de busca el año
    dato = cstr_formato.__format__('%Y')

    # print(dato)
    return dato


def hash(dato):
    '''
        funcion que hashea un dato

        input:
          dato(str): dato que se quiere hashear

        output:
          value(str) - dato hasheado
    '''



    # El dato Unicode debe ser codificado usando encode convirtiendolo en una cadena que no es un string
    # El método de bytes () devuelve un objeto de bytes que es una secuencia inmutable (no se puede modificar)
    dato_in = bytes(dato, 'utf-8')

    # Se Genera la sal por primera vez
    # sal = bcrypt.gensalt(10)
    # print('newSAlt:', sal)

    # Despues de obtenerla, la sal es:
    sal_str = '$2b$10$FX2.2O/0kB29EstQnMNQ8O'
    sal = bytes(sal_str, 'utf-8')
    # print('sal: ', sal)

    # El dato es hasheado
    hashed = bcrypt.hashpw(dato_in, sal)

    # el has se pasa a str
    hashed_str = hashed.decode("utf-8")
    # print('total: ', hashed_str)

    # la codificacion devuelve un obejeto bytes que al inicio contiene la sal, por lo cual
    # es necesario identificarlo y solo enviar el str restante
    valor = hashed_str[29:]

    # print('hash: ', valor)
    return valor

def verificarhash(hashed_in, password):

    '''
        funcion que verifica si un dato hasheado

        input:
          hashed(str): dato hasheado -- solo el string

        output:
          passw(boolean) - Si es correcto pasa true de lo contrario false
    '''

    # El dato Unicode debe ser codificado usando encode convirtiendolo en una cadena que no es un string
    # El método de bytes () devuelve un objeto de bytes que es una secuencia inmutable (no se puede modificar)
    password = bytes(password, 'utf-8')
    sal_str = '$2b$10$FX2.2O/0kB29EstQnMNQ8O'
    print(password)

    hashed = sal_str + hashed_in
    hashed_bytes = bytes(hashed, 'utf-8')
    # print('hashed_bytes: ', hashed_bytes)

    # Se verifica el dato hasheado
    if bcrypt.checkpw(password, hashed_bytes):
        passw = bcrypt.checkpw(password, hashed_bytes)
        print("It Matches!")
        print('password: ', passw)
        return passw
    else:
        print("It Does not Match :(")
        return 'NA'
#
# hashed = hash('1990')


def hashBaseDatos(dato):
    hashed = hash(dato)
    hashed2 = hash(hashed)

    return hashed2

def hashlog(dato):
    hashed = hash(dato)

    return hashed
