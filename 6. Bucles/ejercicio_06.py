#Calculadora
opcion = None
while opcion != 5:
    print("""OPERACIONES A REALIZAR: 
    1. SUMA
    2. RESTA
    3. MULTIPLICACION
    4. DIVISION
    5. SALIR""")
    opcion = int(input("Elige una opcion: "))
    if opcion == 1:
        numero1 = int(input("Valor 1: "))
        numero2 = int(input("Valor 2: "))
        print("Suma =", (numero1 + numero2))
    elif opcion == 2:
        numero1 = int(input("Valor 1: "))
        numero2 = int(input("Valor 2: "))
        print("Resta =", (numero1 - numero2))
    elif opcion == 3:
        numero1 = int(input("Valor 1: "))
        numero2 = int(input("Valor 2: "))
        print("Multiplicacion =", (numero1 * numero2))
    elif opcion == 4:
        numero1 = int(input("Valor 1: "))
        numero2 = int(input("Valor 2: "))
        print("Division =", (numero1 / numero2))
    elif opcion == 5:
        print("Saliendo del sistema")
    else:
        print("Valor no valido")

persona = "hola"
len(persona)