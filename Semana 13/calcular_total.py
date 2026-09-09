# Programa que calcula el total de una compra en una tienda

# Definición de la función con dos parámetros
def calcular_total(precio, cantidad):
    """
    Calcula el total de una compra multiplicando el precio por la cantidad.
    
    Parámetros:
        precio (float): Precio unitario del producto.
        cantidad (int): Cantidad de productos a comprar.
    
    Retorna:
        float: El total de la compra.
    """
    total = precio * cantidad
    return total


# Bloque principal del programa
if __name__ == "__main__":
    precio = 25.50
    cantidad = 4
    
    resultado = calcular_total(precio, cantidad)
    
    print("=== TIENDA ===")
    print(f"Precio unitario: ${precio}")
    print(f"Cantidad: {cantidad}")
    print(f"Total a pagar: ${resultado}")