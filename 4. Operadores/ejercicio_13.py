valor_minimo = 0
valor_maximo = 5

valor_ingresado = int(input("Numero (0-5): "))
valido = (valor_ingresado >= valor_minimo and
          valor_ingresado <= valor_maximo)

print("Está en el rango:", valido)