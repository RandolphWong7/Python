# Programa para gestionar las notas de los estudiantes usando un diccionario

def main():
    # 1. Creación de la colección de datos (Diccionario)
    # La clave será el nombre del estudiante y el valor será su nota
    notas_estudiantes = {}

    while True:
        print("\n--- SISTEMA DE NOTAS ---")
        print("1. Agregar estudiante y nota")
        print("2. Mostrar todos los estudiantes")
        print("3. Buscar nota de un estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del estudiante: ")
            nota = float(input("Ingrese la nota (0-10): "))
            
            # Asignar valor al diccionario
            notas_estudiantes[nombre] = nota
            print(f"✅ Estudiante '{nombre}' agregado con nota {nota}.")

        elif opcion == '2':
            print("\n--- Lista de Estudiantes ---")
            if not notas_estudiantes:
                print("No hay estudiantes registrados.")
            else:
                for nombre, nota in notas_estudiantes.items():
                    print(f"Nombre: {nombre} | Nota: {nota}")

        elif opcion == '3':
            nombre = input("Ingrese el nombre del estudiante a buscar: ")
            if nombre in notas_estudiantes:
                print(f"La nota de {nombre} es: {notas_estudiantes[nombre]}")
            else:
                print(f"El estudiante '{nombre}' no está registrado.")

        elif opcion == '4':
            nombre = input("Ingrese el nombre del estudiante a eliminar: ")
            if nombre in notas_estudiantes:
                del notas_estudiantes[nombre]
                print(f"Estudiante '{nombre}' eliminado correctamente.")
            else:
                print(f"El estudiante '{nombre}' no está registrado.")

        elif opcion == '5':
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()