# Uso de listas

lista= [1,2,3,4,5]
print(f"{lista} -> Lista original")

# Largo de la lista
print(f"Largo de la lista: {len(lista)}")

# Elementos segun indice
print(f'Valor del indice 4: {lista[4]}')
print(f'Valor del ultimo indice: {lista[-1]}')

# Cambiar elementos de lista
lista[1] = 13
print(f"Indice 1 modificado: {lista[1]}")

# Agregar al final de la lista
lista.append(6)
print(f'{lista} -> numero 6 agregado')

# Añadir un nuevo elemento en un indice especifico
lista.insert(2,5)
print(f'{lista} -> numero 15 agregado en el indice 2')

# Eliminar elemento de una lista
# Remove
lista.remove(5) # Quita un 5, no ambos
print(f'{lista} -> numero 5 eliminado')
# Pop
lista.pop(1) # Quita el indice 1
print(f'{lista} -> indice 1 eliminado')
# Del ( delete)
del lista[2]
print(f'{lista} -> indice 2 eliminado')

# Obtener sublistas
sublista = lista [1:3] # lista del 1 al 2( el 3 no incluye)
print(f'Sublista [1:3]: {sublista}')