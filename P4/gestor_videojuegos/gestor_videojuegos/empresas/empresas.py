import funciones
from empresas import crud
import pandas as pd
from fpdf import FPDF

def menuEmpresas():
    print("=" * 80)
    funciones.centrar("૮︵⭒‿᧔ MENU DE EMPRESAS ᧓‿⋆︵౨ \n")
    print("=" * 80)
    opcion=input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Buscar \n\t 6.- Vaciar \n\t 7.- Convertir a texto\n\t 8.- Salir \n \t\tElige una Opcion: ").strip()
    return opcion

def agregarEmpresas(nombre, año_fundacion, pais_origen, conexionBD):
    funciones.centrar("૮︵⭒‿᧔ AGREGAR EMPRESAS ᧓‿⋆︵౨ \n")
    opc="si"
    while opc=="si":
        nombre=input("―୨୧⋆ ˚Nombre de la empresa a agregar: ").strip()
        año_fundacion = crud.regex_validacion()
        pais_origen=input("―୨୧⋆ ˚País de origen de la empresa: ").upper().strip()
        respuesta=crud.insertar(nombre, año_fundacion, pais_origen, conexionBD)
        if respuesta:
            funciones.accionExitosa()
            opc=input("―୨୧⋆ ˚¿Deseas agregar otra empresa (si/no)? ").lower().strip()
        else:
            funciones.accionNoExitosa()
            respuesta=input("―୨୧⋆ ˚¿Desea intentar de nuevo (si/no)? ").lower().strip()
    funciones.esperarTecla()   

def mostrarEmpresas(conexionBD):
    print("=" * 80)
    funciones.centrar("૮︵⭒‿᧔ MOSTRAR EMPRESAS ᧓‿⋆︵౨ \n")
    print("=" * 80)
    empresas=crud.consultar(conexionBD)
    contador=0
    suma_años=0

    for empresa in empresas:

        contador += 1
    if len(empresas)>0:
        lista_empresas=[]
    for i in empresas:
        lista_empresas.append(i[1])
    if len(empresas)>0:
        print("\n" + "="*80)
        print(f"{'Codigo':<10}{'Empresa':<25}{'Año fundación':<20}{'Pais origen':<20}")
        print("="*80)

        for i in empresas:
            print(f"{i[0]:<10}{i[1]:<25}{i[2]:<20}{i[3]:<20}")

        print("="*80)
    else:
        print("── ⋅ ¡No hay empresas que Mostrar, verifique! ⋅ ──")
    funciones.esperarTecla()
    
def buscarEmpresas(conexionBD):
    print("=" * 80)
    funciones.centrar("૮︵⭒‿᧔ BUSCAR EMPRESAS ᧓‿⋆︵౨ \n")
    print("=" * 80)
    nombre=input("―୨୧⋆ ˚Escribe el empresas a a buscar: ").upper().strip()
    empresas=crud.buscar(nombre,conexionBD)
    if len(empresas)>0:
        print("\n" + "="*80)
        print(f"{'Codigo':<10}{'Empresa':<25}{'Año fundación':<20}{'Pais origen':<20}")
        print("="*80)

        for i in empresas:
            print(f"{i[0]:<10}{i[1]:<25}{i[2]:<20}{i[3]:<20}")

        print("="*80)
    else:
        print("── ⋅ ¡No se encontro la empresaque estas buscando, verifique! ⋅ ── ")
    funciones.esperarTecla()

def borrarEmpresass(conexionBD):
    print("=" * 80)
    funciones.centrar("૮︵⭒‿᧔ BORRAR EMPRESAS ᧓‿⋆︵౨ \n")
    print("=" * 80)
    nombre=input("―୨୧⋆ Escribe el empresas: ").upper().strip()
    empresas=crud.buscar(nombre,conexionBD)
    if len(empresas)>0:
        print("\n" + "="*80)
        print(f"{'Codigo':<10}{'Empresa':<25}{'Año fundación':<20}{'Pais origen':<20}")
        print("="*80)

        for i in empresas:
            print(f"{i[0]:<10}{i[1]:<25}{i[2]:<20}{i[3]:<20}")

        print("="*80)
        opc=""
        while opc!="si":
         opc=input("―୨୧⋆ ¿estas seguro que deseas borrar el Empresas de tu lista (si/no)?").lower().strip()
        if opc=="si":
          respuesta=crud.borrar(nombre,conexionBD)
          if respuesta:
           funciones.accionExitosa()
          else:
           funciones.accionNoExitosa
    else:
        funciones.centrar("── ⋅ ¡No se encontro el Empresas que estas buscando, verifique! ⋅ ── ")
    funciones.esperarTecla()  
        
def modificarEmpresas(conexionBD):
    print("=" * 80)
    funciones.centrar("૮︵⭒‿᧔ MODIFICAR EMPRESAS ᧓‿⋆︵౨ \n")
    print("=" * 80)
    nombre_old=input("―୨୧⋆ Escribe el nombre de la empresa a modificar: ").upper().strip()
    empresas=crud.buscar(nombre_old,conexionBD)
    if len(empresas)>0:
        print("\n" + "="*80)
        print(f"{'Codigo':<10}{'Empresa':<25}{'Año fundación':<20}{'Pais origen':<20}")
        print("="*80)

        for i in empresas:
            print(f"{i[0]:<10}{i[1]:<25}{i[2]:<20}{i[3]:<20}")

        print("="*80)
        opc=""
        while opc!="si":
         opc=input("―୨୧⋆ ¿estas seguro que deseas modificar el empresas (si/no)?").lower().strip()
        if opc == "si":
         nv_nombre = input("―୨୧⋆ Escribe el nuevo nombre de la empresa: ").upper().strip()
         año_fundacion = crud.regex_validacion()
         pais_origen = input("―୨୧⋆ Escribe el país de origen: ").upper().strip()
         respuesta = crud.modificar(nombre_old,año_fundacion,pais_origen,nv_nombre,conexionBD)
        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNoExitosa()
    else:
            print("── ⋅ ¡No se encontro el empresas que estas buscando, verifique! ⋅ ── ")
            funciones.esperarTecla()  

def limpiarEmpresas(conexionBD):
    print("=" * 80)
    funciones.centrar("૮︵⭒‿᧔ BORRAR TODAS LAS EMPRESAS ᧓‿⋆︵౨ \n")
    print("=" * 80)
    opc=""
    while opc!="si" and opc!="no":
       opc=input("―୨୧⋆ ¿estas seguro que deseas borrar TODAS las empresas (si/no)?").lower().strip()
    if opc=="si":
        respuesta=crud.vaciar(conexionBD)
        if respuesta:
           funciones.accionExitosa()
        else:
           funciones.accionNoExitosa
    funciones.esperarTecla()

def obtener_datos_db():
    conexionBD = funciones.conectar() 
    query = "SELECT * FROM empresas" 
    df = pd.read_sql_query(query, conexionBD)
    conexionBD.close()
    return df

def exportar_desde_db():
    try:
        funciones.borrarPantalla()
        try:
            df = obtener_datos_db()
        except Exception as e:
            print(f"―୨୧⋆ Error al conectar a la base de datos: {e}")
            input("\nPresiona cualquier tecla para regresar...")
            return

        print("==========================================")
        print("  EXPORTAR DATOS DE LA BASE DE DATOS      ")
        print("==========================================")
        print("¿A qué formato deseas exportar la información?")
        print("  1. Texto plano (.txt)")
        print("  2. Excel (.xlsx)")
        print("  3. Documento (.pdf)")

        try:
            opcion = int(input("\nElige una opción: "))
        except ValueError:
            print("\nOpción no válida. Debes ingresar un número.")
            input("\nPresiona cualquier tecla para continuar...")
            return
        nombre_salida = "Empresas_db"
        match opcion:
            case 1:
                funciones.borrarPantalla()
                archivo_txt = f"{nombre_salida}.txt"
                df.to_csv(archivo_txt, sep='\t', index=False) 
                print(f"\n Datos exportados con éxito a: {archivo_txt}")
                
            case 2:
                funciones.borrarPantalla()
                archivo_excel = f"{nombre_salida}.xlsx"
                df.to_excel(archivo_excel, index=False)
                print(f"\n Datos exportados con éxito a: {archivo_excel}")
                
            case 3:
                funciones.borrarPantalla()
                archivo_pdf = f"{nombre_salida}.pdf"
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Times", size=10)
                
                texto_tabla = df.to_string(index=False)
                for linea in texto_tabla.splitlines():
                    linea_limpia = linea.encode('latin-1', 'replace').decode('latin-1')
                    pdf.cell(0, 8, txt=linea_limpia, ln=True)    
                
                pdf.output(archivo_pdf)
                print(f"\nDatos exportados con éxito a: {archivo_pdf}")
                
            case _:
                print("\n Opción no válida.")
        input("\nPresiona cualquier tecla para regresar al menú principal...")

    except Exception:
        funciones.opcionInvalida()
if __name__ == "__main__":
    exportar_desde_db()