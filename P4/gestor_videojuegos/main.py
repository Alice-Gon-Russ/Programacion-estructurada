import funciones
from videojuegos import videojuegos
from empresas import empresas

resp="1"
repeticiones=0
conexionBD=funciones.conectar()
nombre=[]
plataformas=[]
idioma=[]
año_fundacion=[]
pais_origen=[]
empresa=[]
nv_nombre=[]
nombre_old=[]


while resp != "3":
    funciones.borrarPantalla()
    resp=funciones.menuPrincipal()

    match resp:
        case "1":
            funciones.borrarPantalla()
            opc=videojuegos.menuVideojuegos()
            match opc:
                case "1":
                    funciones.borrarPantalla()
                    videojuegos.agregarVideojuegos(nombre, plataformas, idioma, empresa, conexionBD)
                case "2":
                    funciones.borrarPantalla()
                    videojuegos.borrarVidejuegos(conexionBD)
                case "3":
                    funciones.borrarPantalla()
                    videojuegos.modificarVidejuegos(conexionBD)
                case "4":
                    funciones.borrarPantalla()
                    videojuegos.mostrarVideojuegos(conexionBD)
                case "5":
                    funciones.borrarPantalla()
                    videojuegos.buscarVideojuegos(conexionBD)
                case "6":
                    funciones.borrarPantalla()
                    videojuegos.limpiarVideojuegos(conexionBD)
                case "7":
                    funciones.borrarPantalla()
                    videojuegos.exportar_desde_db()
                case "8":
                    funciones.borrarPantalla()
                    funciones.terminar()
                case _:
                    funciones.borrarPantalla()
                    funciones.opcionInvalida()
        case "2":
            funciones.borrarPantalla()
            opc_sub=empresas.menuEmpresas()
            match opc_sub:
                            case "1":
                                funciones.borrarPantalla()
                                empresas.agregarEmpresas( nombre,año_fundacion, pais_origen,conexionBD)
                            case "2":
                                funciones.borrarPantalla()
                                empresas.borrarEmpresas(conexionBD)
                            case "3":
                                funciones.borrarPantalla()
                                empresas.modificarEmpresas(conexionBD)
                            case "4":
                                funciones.borrarPantalla()
                                empresas.mostrarEmpresas(conexionBD)
                            case "5":
                                funciones.borrarPantalla()
                                empresas.buscarEmpresas(conexionBD)
                            case "6":
                                funciones.borrarPantalla()
                                empresas.limpiarEmpresas(conexionBD)
                            case "7":
                                funciones.borrarPantalla()
                                empresas.exportar_desde_db()
                            case "8":
                                funciones.borrarPantalla()
                                funciones.terminar()
                            case _:
                                funciones.borrarPantalla()
                                funciones.opcionInvalida()
        case "3":
          repeticiones += 1
          print("Cantidad de veces utilizado:", repeticiones)
          funciones.terminar()
                
