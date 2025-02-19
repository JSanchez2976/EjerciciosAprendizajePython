# Generador de ID
import random

nombre = input(f'Nombre = ')
apellido = input(f'Apellido = ')
año_nacimiento = input(f'Año nacimiento = ')
aleatorio = random.randint(1000,9999)

id_generado = (nombre[0:2].upper()+apellido[0:2].upper()
               +año_nacimiento[2:]+str(aleatorio))

print(f'Tu id es:',id_generado)