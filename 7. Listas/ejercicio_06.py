# Desempaquetado de tuplas    Unpacking

producto = ("P001","Pantalon",25.50)

# Desempaquetado
id, descripcion, precio = producto

# Valores
print(f'Tupla completa: {producto}')
# Valores independientes desempaquetados
print(f"Producto: id = {id}, descripcion = {descripcion}, precio = {precio:.2f} €")