# Playlist canciones

# Crear lista
lista_reproduccion = []

n_canciones=int(input("Cuantas canciones quieres: "))

# Iterar para agregar elementos
for indice in range(n_canciones):
    cancion= input(f"Cancion {indice+1}: ")
    lista_reproduccion.append(cancion)

# ordenar en orden alfabetico (sort)
lista_reproduccion.sort()
#lista_reproduccion.sort(reverse=True) así es al revés

# mostrar iterando sus elementos
print("\nLista de reproduccion iterada: ")
for elementos in lista_reproduccion:
    print(elementos)