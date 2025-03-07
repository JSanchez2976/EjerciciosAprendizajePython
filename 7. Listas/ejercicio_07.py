# Combinacion de listas y tuplas
from ejercicio_06 import descripcion

# lista q almacena tuplas de productos
# esto es debido a que, la lista si q se puede modificar pero los valores
# de producto no deberían modificarse
productos = [
    ("P001","Camiseta",20.00),
    ("P002","Pantalones",30.00),
    ("P003","Sudadera",40.00),
]

# Imprimir la informacion de cada uno
# Sacar precio total
precio_total = 0
print("Informacion de productos: ")
for elementos in productos:
    #print(elementos)
    id,descripcion,precio = elementos # unpacking
    print(f'Producto: id= {id}, descripcion= {descripcion}, precio = {precio:.2f}€')
    precio_total+=precio; # producto[2]
print(f"El precio total es: {precio_total} €")
