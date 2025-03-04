# Promedio de notas

notas = []

while True:
    cantidad = int(input("Cuantas notas vas a meter: "))
    if 1<= cantidad <=10:
        break
    print("Numeros no validos (0-10)")

# Rellenar
for indice in range(cantidad):
    while True:
        nota = int(input(f"Nota {indice + 1} = "))
        if 1 <= nota <=10:
            break
        print("La nota debe estar comprendida entre (1-10)")
    notas.append(nota)
    #Suma
    # suma += nota      // Así se hace en java

print(f"Las notas proporcionadas son: {notas}")
suma = sum(notas)   # Para
# Media
media = suma / cantidad

print(f"\nLa media es: {media:.2f}")