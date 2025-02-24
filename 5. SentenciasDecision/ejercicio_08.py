# Sistema reserva hotel

nombre = input("Nombre del cliente: ")
dias = int(input("Cuantos dias vas a estar: "))
cuarto_vista_mar = input("Cuarto con vista al mar (Si/No): ").strip().lower()

cuarto_vista_mar = cuarto_vista_mar == 'si'

if cuarto_vista_mar:
    precio = 190.50
else:
    precio = 150.50

total = dias * precio

print("------ RESUMEN ESTANCIA ------")
print("Nombre =",nombre)
print("Dias =",dias)
print(f"Total a pagar = {total:.2f}€")
if cuarto_vista_mar:
    print("Cuarto con vistas al mar")
else:
    print("Cuarto sin vistas al mar")