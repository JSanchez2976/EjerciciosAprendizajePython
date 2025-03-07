# Manejo de tuplas

tupla = (1,2,3,4,5)
print(tupla)
# No se puede modificar
# tupla[0]=1      ERROR

# Iterar elementos
for elemento in tupla:
    print(elemento, end=" ")

# Crear una tupla para coordenada x,y
coordenadas=(3,5)
# Acceder a los elementos
print(f'\nEje x: {coordenadas[0]}')
print(f'Eje y: {coordenadas[1]}')

# Crear una tupla de un solo elemento
tupla_unico_elemento = 10, # Obligatorio poner la coma
print(f'Tupla un elemento: {tupla_unico_elemento}')

# Tupla anidada
tupla_anidada = (1,(3,4),(5,6))

print(f"El segundo elemento de la tupla anidada es: {tupla_anidada[1]}")