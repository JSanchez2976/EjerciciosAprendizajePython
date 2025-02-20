# Operador not
from ejercicio_04 import resultado

condicion1 = True
resultado = not condicion1
print(f'Not frente a {condicion1}: {resultado}')

# Mirar si una cadena está vacia
nombre = ""
esta_vacia = not nombre
print(f'Está vacia la cadena?: {esta_vacia}')

# Mirar si una variable no tiene valor asignado
variable = None
esta_vacia = not variable
print(f'Está vacia la variable?: {esta_vacia}')