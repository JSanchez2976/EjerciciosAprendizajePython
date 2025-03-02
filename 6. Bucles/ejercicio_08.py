# Adivinar numero
from random import randint
INTENTOS_MAX=10
numero = randint(1,50)
acertado = False
intentos= 0
while not acertado and intentos < INTENTOS_MAX:
    opcion = int(input("Introduce el numero que creas(1-50): "))
    intentos+=1
    if opcion < numero:
        print(f"El numero a adivinar es mayor de {opcion}\n")
    elif opcion > numero:
        print(f"El numero a adivinar es menor de {opcion}\n")
    else:
        print("Felicidades has acertado el número!")
        print(f"Numero de intentos: {intentos}")
        acertado=True

if intentos==INTENTOS_MAX:
    print(f"FIN, has agotados los {INTENTOS_MAX} intentos")