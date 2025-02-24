# Aplicar logica inversa (NOT)

print("*** PARQUE DE ATRACCIONES ***")

edad = int(input("Edad: "))
miedo = input("Tienes miedo a la oscuridad: ")

tiene_miedo = miedo.strip().lower() == 'si'
edad_valida = edad > 10

if not tiene_miedo and edad_valida:
    print("Adelante, puedes pasar")
else:
    print("Lo siento, no puedes pasar")