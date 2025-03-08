# Manejo de sets    Utiles para cuando no quieres repetir
# los sets no funcionan por indices

# Crear un conjunto
ejemplo_set = {1,2,3,4,5,4}
print(f'Set: {ejemplo_set}')

# Agregar elementos al set
ejemplo_set.add(6)
ejemplo_set.add(7)


# Intentar con elemento duplicado
ejemplo_set.add(3)


# Eliminar un elemento del conjunto
ejemplo_set.remove(4)
print(f'Set modificado: {ejemplo_set}')

# Iterar elementos del set
for elemento in ejemplo_set:
    print(elemento,end=" ")

# Comprobar si existe elemento en el set
print(f"\nExiste el valor 4 en mi set? {4 in ejemplo_set}")

# Obtener longitud del set
print(f'Longitud del conjunto: {len(ejemplo_set)}')