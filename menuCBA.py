'''
Centro de Biotecnologia Agropecuaria
fecha: 06/05/2024
aprendiz: Julian Daniel Camacho Aguilar
ficha: 2877795
version: 3.12.3
'''

from funcionesMENU import *

if __name__ == "__main__":
    preguntar = True
    estudiantes = [] 

# creamos la lógica de la selección del número
    while preguntar:
        # creamos un try-except para el manejo de errores.
        try:
            mostrar_menu()
            opcion = int(input("Seleccione la opción a la que desea ingresar según su número: "))

            # creamos la logica de opcion 1        
            if opcion == 1:
                estudiantes = parametrizar()
                print("__________________________________________")
                input("Se parametrizó correctamente, Presione Enter para mostrar el menú.")
                

            # creamos la logica de opcion 2
            elif opcion == 2:
                ingresar_aprendiz(estudiantes)
                print("__________________________________________")
                respuesta = input("Estudiante agregado, presione x para volver al menú: ").lower()
                while respuesta not in ["x"]:
                    print("CARACTER INVÁLIDO, INTENTE DE NUEVO")
                    respuesta = input("Estudiante agregado, presione x para volver al menú:").lower() 

            # creamos la logica de opcion 3            
            elif opcion == 3:
                print("__________________________________________")
                mostrar_aprendices(estudiantes)
                input("Presione enter para mostrar el menú.")
                

            # creamos la logica de opcion 4
            elif opcion == 4:
                print("__________________________________________")
                print("Resultado por fichas:")
                mostrar_resultado_por_fichas(estudiantes)
                input("Presione enter para mostrar el menú.")
                

            # creamos la logica de opcion 5
            elif opcion == 5:
                print("__________________________________________")
                mostrar_aprendices_aprobados(estudiantes)
                input("Presione Enter para mostrar el menú.")
                

            # creamos la logica de opcion 6
            elif opcion == 6:
                print("__________________________________________")
                mostrar_aprendices(estudiantes)  # Mostrar lista de aprendices antes de borrar
                documento_a_borrar = int(input("Ingrese el documento del estudiante que desea borrar: "))
                for i, estudiante in enumerate(estudiantes):
                    if estudiante["documento"] == documento_a_borrar:
                        del estudiantes[i]
                        print("El estudiante ha sido eliminado correctamente.")
                        break
                else:
                    print("No se encontró el documento especificado.")
                input("Presione Enter para mostrar el menú.")
                

            # creamos la logica de opcion 7
            elif opcion == 7:
                print("__________________________________________")
                mostrar_aprendices(estudiantes)  # Mostrar lista de aprendices antes de editar
                editar_informacion(estudiantes)
                input("Presione Enter para mostrar el menú.")
                    
            # creamos la logica de opcion 0
            elif opcion == 0:
                print("__________________________________________")
                print("---FIN DEL MENU---")
                preguntar = False

        except ValueError:
            print("--CARACTER INVALIDO, INTENTE DE NUEVO--")

'''
cuadrar que cuando oprima enter se ve 2 veces el menu
'''            