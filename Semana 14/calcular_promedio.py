# Programa que calcula el promedio de tres notas

# Definición de la función con tres parámetros
def calcular_promedio(nota1, nota2, nota3):
    """
    Calcula el promedio de tres notas.
    
    Parámetros:
        nota1 (float): Primera nota.
        nota2 (float): Segunda nota.
        nota3 (float): Tercera nota.
    
    Retorna:
        float: El promedio de las tres notas.
    """
    # Realiza el cálculo matemático
    promedio = (nota1 + nota2 + nota3) / 3
    
    return promedio


# Bloque principal del programa
if __name__ == "__main__":
    # Asignación de valores a las notas
    nota1 = 9.0
    nota2 = 7.0
    nota3 = 8.5
    
    # Llamada a la función y almacenamiento del resultado
    resultado = calcular_promedio(nota1, nota2, nota3)
    
    # Mostrar el resultado en consola
    print("=== CÁLCULO DE PROMEDIO ===")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"El promedio final es: {resultado:.2f}")