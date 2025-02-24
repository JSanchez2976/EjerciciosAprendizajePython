# Sacar numero mayor

numero1 = int(input("Introduce un número entero: "))
numero2 = int(input("Introduce otro número entero: "))

if numero1>numero2:
    print(f"El numero mayor es: {numero1}")
elif numero2>numero1:
    print(f"El numero mayor es: {numero2}")
else:
    print("Los numeros son iguales")