# Programa que simula la reserva de asientos en una sala de cine de 3 filas x 4 columnas

def main():
    # 1. Crear la matriz de asientos (3 filas x 4 columnas) inicializada en 0
    # 0 = asiento libre, 1 = asiento reservado
    asientos = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    print("=== SALA DE CINE ===")
    print("Filas: 0 a 2 | Columnas: 0 a 3")
    print("0 = Libre | 1 = Reservado\n")

    # 2. Solicitar la fila al usuario con validación
    while True:
        fila = int(input("Ingrese el número de fila (0 a 2): "))
        if 0 <= fila <= 2:
            break
        print("Fila no válida. Debe estar entre 0 y 2.")

    # 3. Solicitar la columna al usuario con validación
    while True:
        columna = int(input("Ingrese el número de columna (0 a 3): "))
        if 0 <= columna <= 3:
            break
        print("Columna no válida. Debe estar entre 0 y 3.")

    # 4. Verificar si el asiento ya está reservado
    if asientos[fila][columna] == 1:
        print(f"\n El asiento en la fila {fila}, columna {columna} ya está reservado.")
    else:
        # 5. Marcar el asiento como reservado (cambiar 0 por 1)
        asientos[fila][columna] = 1
        print(f"\nAsiento reservado correctamente en la fila {fila}, columna {columna}.")

    # 6. Mostrar el estado completo de la sala usando bucles anidados
    print("\n--- Estado de la sala ---")
    for i in range(3):
        for j in range(4):
            print(asientos[i][j], end="  ")
        print()

# Llamada a la función principal
if __name__ == "__main__":
    main()