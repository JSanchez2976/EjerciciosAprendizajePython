# Descuentos

n_productos_descuento = 10
cantidad_productos = int(input('Cuantos productos compraste hoy: '))
tiene_membresia= input('Tienes la membresía de la tienda (Si/No)? ')

descuento_posible = (cantidad_productos >= n_productos_descuento
                     and tiene_membresia.strip().lower() == 'si')

print(f'Tiene acceso a descuento: {descuento_posible}')