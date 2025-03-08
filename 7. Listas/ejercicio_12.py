# Diccionario en Python

# Crear diccionario persona con su clave y valor
# Al igual que los sets, no permite duplicados
persona = {
    "nombre": "Jorge",
    "edad": 18,
    "pais": "España"
}
print(f"Diccionario de persona: {persona}")

# Acceder a los elementos del diccionario
print(f'Nombre: {persona["nombre"]}')
print(f'Edad: {persona.get("edad")}')

# Modificar un valor del diccionario
persona["edad"] = 35    # En el caso de no existir "edad" crearía el campo
print(f"Diccionario de persona: {persona}")

# Agregar elemento
persona["trabajo"] = "Developer"
print(f"Diccionario de persona: {persona}")

# Eliminar un elemento
del persona["pais"]
print(f"Diccionario de persona: {persona}")

# Al igual que con listas está el metodo pop
persona.pop("trabajo")
print(f"Diccionario de persona: {persona}")

# Iterar los elementos del diccionario (llave, valor)
for llave, valor in persona.items():
    print(f"Llave: {llave}, valor: {valor}")

# Obtener los valores
print(f'\nValores del diccionario: ')
for valor in persona.values():
    print(f'Valor: {valor}')

# Obtener las llaves
print(f'\nLlaves del diccionario: ')
for llaves in persona.keys():
    print(f"Llave: {llaves}")