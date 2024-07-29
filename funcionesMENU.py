'''
Centro de Biotecnologia Agropecuaria
fecha: 06/05/2024
aprendiz: Julian Daniel Camacho Aguilar
ficha: 2877795
version: 3.12.3
'''

# creamos el menu
def mostrar_menu():
    print("______________________________________________________")
    print("Bienvenido al menu del SENA CBA:")
    print("1) Parametrizar")
    print("2) Ingresar aprendiz")
    print("3) Lista de aprendices")
    print("4) Lista por fichas")
    print("5) Resultado de aprendices aprobados por fichas")
    print("6) Borrar aprendiz")
    print("7) Actualizar información")
    print("0) Salir")

# creamos parametrizar
def parametrizar():
    estudiantes = []
    return estudiantes

# creamos el ingreso del estudiante
def ingresar_aprendiz(estudiantes):
    print("Está registrando los datos de un nuevo aprendiz...")
    estudiante = {
        "documento": int(input("Ingrese el número de documento de identidad del aprendiz: ")),
        "nombre": input("Ingrese el nombre del aprendiz: "),
        "ficha": int(input("Ingrese el número de ficha (cocina: 2493512), (comercio: 2917336), (ADSO: 2877795): ")),
        "evaluacion": input("Ingrese la evaluación (a = aprobó) (d = desaprobó): ")
    }

    while estudiante["ficha"] not in [2493512, 2917336, 2877795]:
        print("FICHA INVÁLIDA, INTENTE NUEVAMENTE")
        estudiante["ficha"] = int(input("Ingrese su número de ficha (cocina: 2493512), (comercio: 2917336), (ADSO: 2877795):"))

    while estudiante["evaluacion"] not in ['a', 'd']:
        print("EVALUACIÓN INVÁLIDA, INTENTE NUEVAMENTE")
        estudiante["evaluacion"] = input("Ingrese su evaluación (a/d): ")

    # almacenamos los datos en la lista de estudiantes
    estudiantes.append(estudiante)

# creamos la funcion que muestra resultados por ficha
def mostrar_resultado_por_fichas(estudiantes):
    # Creamos un diccionario para almacenar los datos por ficha
    datos_por_ficha = {}
    for estudiante in estudiantes:
        ficha = estudiante["ficha"]
        if ficha not in datos_por_ficha:
            datos_por_ficha[ficha] = []
        datos_por_ficha[ficha].append(estudiante)

    # Imprimimos los datos organizados por ficha
    for ficha, datos in datos_por_ficha.items():
        print(f"Ficha: {ficha}")
        if datos:
            for estudiante in datos:
                print(f"Documento: {estudiante['documento']}, Nombre: {estudiante['nombre']}, Evaluación: {estudiante['evaluacion']}")
        else:
            print("No hay estudiantes para mostrar...")
        print("-----------------------------------------------------------------------")

# creamos la funcion para condicionar y mostrar solo a los estudiantes que tienen "a"
def mostrar_aprendices_aprobados(estudiantes):
    datos_por_ficha = {}
    for estudiante in estudiantes:
        ficha = estudiante["ficha"]
        if ficha not in datos_por_ficha:
            datos_por_ficha[ficha] = {"aprobados": [], "desaprobados": []}
        if estudiante["evaluacion"] == 'a':
            datos_por_ficha[ficha]["aprobados"].append(estudiante)
        else:
            datos_por_ficha[ficha]["desaprobados"].append(estudiante)

    # Imprimimos los datos organizados por ficha y evaluación
    for ficha, datos in datos_por_ficha.items():
        print(f"Ficha: {ficha}\n")
        print("ESTUDIANTES APROBADOS")
        print("-----------------------------------------------------------------------")
        if datos["aprobados"]:
            for estudiante in datos["aprobados"]:
                print(f"Documento: {estudiante['documento']}, Nombre: {estudiante['nombre']}, Evaluación: {estudiante['evaluacion']}")
        else:
            print("No hay estudiantes para mostrar en esta seccion")
        print("-----------------------------------------------------------------------\n")
        print("ESTUDIANTES DESAPROBADOS")
        print("-----------------------------------------------------------------------")
        if datos["desaprobados"]:
            for estudiante in datos["desaprobados"]:
                print(f"Documento: {estudiante['documento']}, Nombre: {estudiante['nombre']}, Evaluación: {estudiante['evaluacion']}")
        else:
            print("No hay estudiantes para mostrar en esta seccion")
        print("-----------------------------------------------------------------------\n")

# re creamos la funcion de editar informacion
def editar_informacion(estudiantes):
    documento_editar = int(input("Ingrese el número de documento del estudiante que desea editar: "))
    for estudiante in estudiantes:
        if estudiante["documento"] == documento_editar:
            print("¿Qué información desea editar?")
            print("1) Nombre")
            print("2) Ficha")
            print("3) Evaluación")
            opcion_editar = int(input("Seleccione una opción: "))
            if opcion_editar == 1:
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                estudiante["nombre"] = nuevo_nombre
                print("Nombre actualizado correctamente.")
            elif opcion_editar == 2:
                nueva_ficha = int(input("Ingrese la nueva ficha (cocina: 2493512), (comercio: 2917336), (ADSO: 2877795): "))
                while nueva_ficha not in [2493512, 2917336, 2877795]:
                    print("FICHA INVÁLIDA, INTENTE NUEVAMENTE")
                    nueva_ficha = int(input("Ingrese la nueva ficha (cocina: 2493512), (comercio: 2917336), (ADSO: 2877795): "))
                estudiante["ficha"] = nueva_ficha
                print("Ficha actualizada correctamente.")
            elif opcion_editar == 3:
                nueva_evaluacion = input("Ingrese la nueva evaluación (a = aprobó) (d = desaprobó): ")
                while nueva_evaluacion not in ['a', 'd']:
                    print("EVALUACIÓN INVÁLIDA, INTENTE NUEVAMENTE")
                    nueva_evaluacion = input("Ingrese la nueva evaluación (a/d): ")
                estudiante["evaluacion"] = nueva_evaluacion
                print("Evaluación actualizada correctamente.")
            break
    else:
        print("No se encontró el documento especificado.")

# creamos la funcion para mostrar los aprendices
def mostrar_aprendices(estudiantes):
    print("Lista de aprendices:")
    for estudiante in estudiantes:
        print(f"Documento: {estudiante['documento']}, Nombre: {estudiante['nombre']}, Ficha: {estudiante['ficha']}, Evaluación: {estudiante['evaluacion']}")
        print("-----------------------------------------------------------------------")