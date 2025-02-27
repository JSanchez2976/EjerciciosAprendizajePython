# Menu interactivo

opcion = None
while opcion != 3:
    print("\t1. Crear cuenta")
    print("\t2. Eliminar cuenta")
    print("\t3. Salir")
    opcion = int(input("Escoge una opcion= "))
    if opcion == 1:
        print("Creando cuenta")
    elif opcion == 2:
        print("Eliminando cuenta")
    elif opcion == 1:
        print("Saliendo del sistema")
    else:
        print("Opcion no valida")
else:
    print("\nBucle acabado")