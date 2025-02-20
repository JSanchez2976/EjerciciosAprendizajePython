numero = 5
print(f'Valor del numero: {numero}')
numero = 7
print(f'Valor del numero: {numero}')
cadena = 'Hola ;)'
print(f'Valor de la cadena: {cadena}')

# Asignacion multiple
x,y,z = 5,"Hola",4.2863
print(f'Valor de x = {x},y = {y}, z = {z:.2f}')

# Asignacion encadenada
a = b = c = 10
print(f'Valor a = {a}, b = {b}, c = {c}')

# Cambio de valores en una variable, sin variables temporales
x, y = 5, 10
print(f'Valores iniciales x = {x}, y = {y}')
x, y = y, x
print(f'Valores invertidos x = {x}, y = {y}')

# Recibir valores de entrada por usuario
nombre, apellido = input('Pon tu nombre y apellido,(separa por coma): ').split(',')
print(f'Nombre = {nombre.strip()}, apellido = {apellido.strip()}')