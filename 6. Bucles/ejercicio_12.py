# Dibujar triangulo
lineas = int(input("Numero de lineas: "))

print("Piramide normal")
for i in range (1, lineas+1):
    espacios= " " * (lineas-i)
    asteriscos = "*" * (2*i-1)
    print(f'{espacios}{asteriscos}')

print("\nPiramide pegada a la izquierda")
for i in range(1,lineas+1):
    asteriscos="*"*i
    print(asteriscos)

print("\nPiramide pegada a la derecha")
for i in range(1,lineas+1):
    espacios = " " * ( lineas-i)
    asteriscos= "*" * i
    print(f'{espacios}{asteriscos}')

print("\nCuadrado")
for i in range (1,lineas+1):
    if i == 1 or i == lineas:
        print("* "*lineas)
    else:
        espacios= " "*(lineas+1)
        print(f"*{espacios}*")
