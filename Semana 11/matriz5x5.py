# Programa para ingresar 25 valores en una matriz de 5x5 y mostrarla

matriz = [[0 for _ in range(5)] for _ in range(5)]

print("--- INGRESO DE DATOS ---")
for i in range(5):
    for j in range(5):
        valor = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
        matriz[i][j] = valor

print("\n--- MATRIZ INGRESADA ---")
for i in range(5):
    for j in range(5):

        print(matriz[i][j], end="\t")
    print()