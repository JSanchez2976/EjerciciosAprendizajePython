# Conversion de tipos de datos

# Convertir de cadena a numero
numero_cadena = '10'
numero_entero = int(numero_cadena)
print(f'Valor en cadena: {numero_cadena}')
print(f'Cadena a entero: {numero_entero}')

# Convertir de cadena a flotante
numero_cadena = '3.14'
numero_flotante = float(numero_cadena)
print(f'Cadena a flotante: {numero_flotante}')

# Convertir numero a cadena
numero_entero=25
numero_cadena = str(numero_entero)
print(f'Numero a cadena: {numero_cadena}')

# Convertir a boolean
# Falso si es 0, cadena vacía, o None
numero_entero=0
booleano= bool(numero_entero)
print(f'Booleano de 0: {booleano}')

numero_entero=5
booleano= bool(numero_entero)
print(f'Booleano de 5: {booleano}')

cadena = '' # El largo de la cadena es 0
booleano= bool(cadena)
print(f'Valor booleano de cadena vacía: {booleano}')

cadena = 'Cadena con valor'
booleano= bool(cadena)
print(f'Valor booleano de cadena no vacía: {booleano}')

variable = None
booleano= bool(variable)
print(f'Valor booleano de None: {booleano}')