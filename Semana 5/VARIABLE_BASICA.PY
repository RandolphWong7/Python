# Solicitar datos al usuario
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))           # input() devuelve texto, por eso usamos int()
estatura = float(input("Ingrese su estatura: ")) # Convertimos a float
estudiante_activo = input("¿Es estudiante activo? (True/False): ")

# texto a booleano
if estudiante_activo.lower() == "true":
    estudiante_activo = True
else:
    estudiante_activo = False

# Mostrar los datos
print("\n--- Información del Estudiante ---")
print("Nombre:", nombre)
print("Edad:", edad)
print("Estatura:", estatura)
print("Estudiante activo:", estudiante_activo)