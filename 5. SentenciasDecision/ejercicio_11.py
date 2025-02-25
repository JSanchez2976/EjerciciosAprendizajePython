# Convertir calificacion numerica a letra

nota = float(input("Introduce la nota(1-10): "))

if 9<= nota <=10:
    nota = 'A'
elif 8 <= nota <9:
    nota = "B"
elif 7<= nota <8:
    nota = "C"
elif 6<= nota <7:
    nota = "D"
elif 0<=nota <6:
    nota="F"
else:
    nota="Valor desconocido"

print("Nota =",nota)