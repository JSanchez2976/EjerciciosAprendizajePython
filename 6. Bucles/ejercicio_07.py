# Contraseña

contraseña_valida = False

while not contraseña_valida:
    contraseña = input("Contraseña(min 6 caracteres): ")
    if len(contraseña)<6:
        print("La contraseña debe tener mas de 6 caracteres")
    else:
        print("Contraseña valida")
        contraseña_valida=True