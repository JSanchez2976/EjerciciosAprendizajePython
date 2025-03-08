# Operaciones con set

a = {1,2,3,4}
b = {3,4,5,6}

union = a | b       # El palito es para unir
print(f'Union de a y b: {union}')

# Valores que coinciden en ambos
interseccion = a & b
print(f'Interseccion a y b: {interseccion}')

# Diferencias (Valores que no coinciden entre dos sets)
diferencia = a-b
print(f'Diferencia a - b: {diferencia}')

diferencia = b-a
print(f"Diferencia b - a: {diferencia}")