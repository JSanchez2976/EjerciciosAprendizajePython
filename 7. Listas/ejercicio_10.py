# Lista suscriptores

suscriptores = {"pepe@gmail.com","pedro@gmail.com","elena@gmail.com"}
print(f'Lista de suscriptores inicial: {suscriptores}')

# Mirar si el suscriptor ya está en la lista
nuevo_suscriptor = "jorge@gmail.com"
if nuevo_suscriptor in suscriptores:
    print(f'El nuevo suscriptor ya está en la lista {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El nuevo suscriptor se ha agregado a la lista {nuevo_suscriptor}')
print(f"Lista de suscriptores: {suscriptores}")

# Eliminar suscriptor
suscriptor_eliminar = "pepe@gmail.com"
suscriptores.remove(suscriptor_eliminar)
print(f'El suscriptor {suscriptor_eliminar} ha sido eliminado')

# Longitud de lista
print(f'Cantidad de seguidores: {len(suscriptores)}')

# Ver valores
print("Lista de suscriptores: ")
for elementos in suscriptores:
    print(elementos)