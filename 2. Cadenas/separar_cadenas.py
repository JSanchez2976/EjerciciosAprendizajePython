# Separar cadenas ( split)

datos="Hola Mundo"
lista = datos.split()# por default separa los elementos por espacios en blanco
print(lista)

datos = 'Juan,30,Mexico'
lista = datos.split(",")
lista[2]="España"
print(lista)
