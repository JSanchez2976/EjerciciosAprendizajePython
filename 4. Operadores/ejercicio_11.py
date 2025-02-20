# Ticket de compra

leche = float(input(f'Introduce el precio de la leche: '))
pan = float(input(f'Introduce el precio del pan: '))
lechuga = float(input(f'Introduce el precio de la lechuga: '))
platanos = float(input(f'Introduce el precio de los platanos: '))

subtotal = leche+pan+lechuga+platanos
impuesto = 0.21 * subtotal
descuento = float(input(f'Introduce el descuento(0-100%): '))
descuento_aplicable = descuento/100 *subtotal
total = subtotal+impuesto-descuento_aplicable

print(f'Subtotal = {subtotal:.2f} €')
print(f'\nImpuestos = {impuesto:.2f} €')
print(f'Descuento = {descuento_aplicable:.2f} €')
print(f'Total = {total:.2f} €')
