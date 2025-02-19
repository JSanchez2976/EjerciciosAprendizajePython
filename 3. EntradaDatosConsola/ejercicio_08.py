print(f'Generador de Email')
nombre = input(f'Nombre = ')
apellidos = input(f'Apellidos = ')
nombre_empresa = input(f'Nombre de la empresa = ')
dominio = input(f'Dominio = ')

# Normalizar

nombre = nombre.lower()
apellidos = apellidos.lower()
nombre_empresa = nombre_empresa.lower()
dominio = dominio.lower()

email = f'{nombre}.{apellidos}@{nombre_empresa}{dominio}'
email = email.replace(" ",".")
print(f'Email generado:',email)
