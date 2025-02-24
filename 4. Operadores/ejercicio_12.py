usuario = "usuario12345"
contraseña = "12345"

usuario_introducido = input("Usuario: ")
contraseña_introducida = input("Contraseña: ")

usuario_valido = usuario == usuario_introducido
contraseña_introducida = contraseña == contraseña_introducida

valido = usuario_valido and contraseña_introducida

print("Datos correctos? ",valido)