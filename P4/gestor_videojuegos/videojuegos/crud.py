def insertar(nombre, plataformas, idioma, empresa, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute(
                "INSERT INTO videojuegos VALUES (NULL, %s, %s, %s, %s)",
                (nombre, plataformas, idioma, empresa),
            )
            conexionBD.commit()
            return True
        return False
    except:
        return False
    
def consultar (conexionBD):
    try:
        if conexionBD!=None:
            cursor=conexionBD.cursor()
            cursor.execute("select * from videojuegos")
            return cursor.fetchall()
        else:
            return []
    except:
        return []

def buscar (nombre,conexionBD):
    try:
        if conexionBD!=None:
            cursor=conexionBD.cursor()
            cursor.execute("select * from videojuegos where nombre=%s", (nombre,))
            return cursor.fetchall()
        else:
            return []
    except:
        return []

def borrar (nombre, conexionBD):
    try:
        if conexionBD!=None:
            cursor=conexionBD.cursor()
            cursor.execute("delete from videojuegos where nombre=%s", (nombre,))
            conexionBD.commit()
            return True
        else:
            return False
    except: 
        return False
    
def modificar(nombre_old, plataformas, idioma, empresa, nv_nombre, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()

            sql = """
            UPDATE videojuegos
            SET nombre=%s,
                plataformas=%s,
                idioma=%s,
                empresa=%s
            WHERE nombre=%s
            """

            cursor.execute(sql, (nv_nombre, plataformas, idioma, empresa, nombre_old))
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
            cursor.execute("truncate videojuegos")
            conexionBD.commit()
            return True
        else:
            return False
    except: 
        return False

