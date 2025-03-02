# Repeticion de un mensaje

mensaje = input("Mensaje a repetir: ")
veces=int(input("Numero de veces: "))

for i in range(veces):
    print(f"{i+1}: {mensaje}")