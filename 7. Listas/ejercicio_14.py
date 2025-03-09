# Lista de diccionarios

personas = [
    {
        "nombre": "Regina",
        "apellido":"Flores",
        "edad": 21
    },
    {
        "nombre":"Alejandro",
        "apellido":"Reyes",
        "edad":32
    },
]

print(personas)

# Acceder a un diccionario desde una lista
print(f'''Primer elemento de la lista:
Nombre: {personas[0].get("nombre")}
Apellido: {personas[0].get("apellido")}
Edad: {personas[0].get("edad")}''')

# Recorrer los elementos de la lista
print()
for contador, elementos in enumerate(personas):
    print(f'{contador} - Persona: {elementos}')