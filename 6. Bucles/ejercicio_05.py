# Sistema bancario

saldo = 1000

opcion = None
while opcion != 4:
    print("""*** OPERACIONES A REALIZAR ***
    1. Consultar Saldo
    2. Retirar
    3. Depositar
    4. Salir""")
    opcion = int(input("Escoje una opcion: "))
    if opcion == 1:
        print(f"Saldo: {saldo}€")
    elif opcion == 2:
        retirado = int(input("Dinero a retirar: "))
        if saldo < retirado:
            print(f"No hay dinero suficiente, {saldo}€ restantes")
        else:
            saldo -= retirado
    elif opcion == 3:
        ingresado = int(input("Dinero a ingresar: "))
        saldo += ingresado
    elif opcion == 4:
        print("Saliendo del sistema")
    else:
        print("Opcion no valida")