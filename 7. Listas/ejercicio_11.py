# Lista suscriptores DINAMICA

# suscriptores = {} # esto crea un diccionario vacio
suscriptores = set()

numero_suscriptores = int(input("Proporciona el numero de suscriptores iniciales: "))
for _ in range (numero_suscriptores):
    suscriptores.add(input("Nuevo suscriptor (email): "))
print(f"Lista de suscriptores inicial: {suscriptores}")

# Crear menú opciones
opcion = None
while opcion != 5:
    print("""1. Ver suscriptores
    2. Añadir suscriptor
    3. Eliminar suscriptor
    4. Modificar suscriptor
    5. Salir """)
    opcion = int(input("Opcion: "))
    if opcion == 1:
       print(f"Lista de suscriptores: {suscriptores}")
    elif opcion == 2:
        añadido = input("Nuevo suscriptor (email): ")
        if añadido in suscriptores:
            print("Ese suscriptor ya estaba añadido")
        else:
            suscriptores.add(añadido)
            print("Añadido correctamente")
    elif opcion == 3:
        eliminado = input("Eliminar suscriptor (email): ")
        if eliminado in suscriptores:
            suscriptores.remove(eliminado)
            print("Eliminado correctamente.")
        else:
            print("No se ha encontrado el suscriptor")
    elif opcion == 4:
        modificado = input("Correo a modificar: ")
        if modificado in suscriptores:
            suscriptores.remove(modificado)
            añadido = input("Nuevo suscriptor (email): ")
            if añadido in suscriptores:
                print("Ese suscriptor ya estaba añadido")
            else:
                suscriptores.add(añadido)
                print("Añadido correctamente")
        else:
            print("No se ha encontrado ese suscriptor")
    elif opcion == 5:
        print("Saliendo del programa")
    else:
        print("Introduce un valor correcto")