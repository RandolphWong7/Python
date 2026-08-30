def main():
    sistema_activo = True 
    tiene_permiso = False 
    
    if sistema_activo:
        if tiene_permiso:
            print("Acción ejecutada")
        else:
            print("Permiso denegado")
    else:
        print("Sistema inactivo")

if __name__ == "__main__":
    main()