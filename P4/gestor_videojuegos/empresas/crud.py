import re
from datetime import datetime

def insertar(nombre, año_fundacion, pais_origen, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute(
                "INSERT INTO empresas VALUES (NULL, %s, %s, %s)",
                (nombre, año_fundacion, pais_origen),
            )
            conexionBD.commit()
            return True
        return False
    except:
        return False


def consultar(conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("SELECT * FROM empresas")
            return cursor.fetchall()
        return []
    except:
        return []


def buscar(nombre, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("SELECT * FROM empresas WHERE nombre=%s", (nombre,))
            return cursor.fetchall()
        return []
    except:
        return []


def borrar(nombre, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("DELETE FROM empresas WHERE nombre=%s", (nombre,))
            conexionBD.commit()
            return True
        return False
    except:
        return False


def modificar(nombre_old, año_fundacion, pais_origen, nv_nombre, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()

            sql = """
            UPDATE empresas
            SET nombre=%s,
                `año de fundación`=%s,
                `pais de origen`=%s
            WHERE nombre=%s
            """
            cursor.execute(sql, (nv_nombre, año_fundacion, pais_origen, nombre_old))
            conexionBD.commit()
            return True
        else:
            return False

    except Exception as e:
        print("Hubo un problema:", e)
        return False

def vaciar(conexionBD):
    try:
        if conexionBD!=None:
            cursor=conexionBD.cursor()
            cursor.execute("truncate empresas")
            conexionBD.commit()
            return True
        else:
            return False
    except: 
        return False
    
def regex_validacion():
    while True:
        año_fundacion = input("―୨୧⋆ Escribe el año de fundación: ").strip()
        if re.fullmatch(r"\d{4}", año_fundacion):
            año = int(año_fundacion)
            if 1800 <= año <= datetime.now().year:
                return año
            else:
                print("El año está fuera del rango permitido")
        else:
            print("Debe ingresar un año válido de 4 dígitos")