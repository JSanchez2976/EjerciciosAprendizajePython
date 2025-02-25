# Sistema autenticación

USUARIO = "pepe"
CONTRASEÑA = "pepe123"

usuario_introducido = input("Usuario= ").lower().strip()
contraseña_introducida = input("Contraseña= ").lower().strip()

if usuario_introducido==USUARIO:
    usuario_valido=True
else:
    usuario_valido=False

if contraseña_introducida==CONTRASEÑA:
    contraseña_valida=True
else:
    contraseña_valida=False

if usuario_valido and contraseña_valida:
    print("Bienvenido al servidor")
elif usuario_valido and not contraseña_valida:
    print("Contraseña incorrecta")
elif not usuario_valido and contraseña_valida:
    print("Usuario incorrecto")
else:
    print("Usuario y contraseña incorrectos")