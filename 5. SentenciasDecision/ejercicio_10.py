# Identificar estacion del año

mes = int(input("En que mes estás (1-12): "))

if mes == 1 or mes == 2 or mes == 12:
    print("La estacion es invierno")
elif mes == 3 or mes == 4 or mes == 5:
    print("La estacion es primavera")
elif mes == 6 or mes == 7 or mes == 8:
    print("La estacion es verano")
elif mes == 9 or mes == 10 or mes == 11:
    print("La estacion es otoño")
else:
    print("Asegurate de poner un mes correcto")