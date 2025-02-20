# Revisar si una variable está entre 1 y 10 con not
dato=int(input('Dame un entero: '))

esta_dentro_rango = 1 <= dato <= 10
print(f'Esta dentro de rango (1 y 10)?: {esta_dentro_rango}')

# Al revés
esta_fuera_rango = not(1<= dato <=10)
print(f'Esta fuera de rango (1 y 10)?: {esta_fuera_rango}')