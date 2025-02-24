miembro = input("Eres miembro de la tienda: ")
miembro = miembro.strip().lower()
es_miembro= miembro == 'si'

cuantia = float(input("Cuanto te has gastado(€): "))

if es_miembro and (cuantia >1000):
    print(f'Tienes un descuento del 10% ({cuantia * 0.1:.2f}€)')
    print(f'Total con descuento: {cuantia - (cuantia *0.1):.2f}')
elif es_miembro:
    print(f'Tienes un descuento del 5% ({cuantia * 0.05:.2f}€)')
    print(f'Total con descuento: {cuantia - (cuantia * 0.05):.2f}')
else:
    print("No tienes ningún descuento")