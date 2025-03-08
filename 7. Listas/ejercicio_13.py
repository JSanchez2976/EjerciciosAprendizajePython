# Agenda de contactos

agenda = {
    "Carlos":{
        "telefono": 165613131,
        "email": "carlos@gmail.com",
        "direccion": "calleCarlos"
    },
    "Maria":{
        "telefono": 654491155,
        "email": "maria@gmail.com",
        "direccion": "calleMaria"
    },
    "Pedro":{
        "telefono": 123456789,
        "email": "pedro@gmail.com",
        "direccion": "callePedro",
    }
}
print(agenda)

# Acceder a un contacto especifico
print(f'''Informacion de María:
    Teléfono: {agenda["Maria"]["telefono"]}
    Email: {agenda.get("Maria").get("email")}
    Direccion: {agenda["Maria"]["direccion"]}
''')

# Agregar un nuevo contacto
agenda["Ana"] = {
    "telefono":1654651,
    "email":"ana@gmail.com",
    "direccion":"calleAna"
}
print(f"Agenda: {agenda}")

# Eliminar un contacto existente
agenda.pop("Pedro")
#del agenda["Pedro"]
print(f"Agenda: {agenda}")

# Mostrar contactos agenda
print("\nContactos de la agenda")
for nombre,detalles in agenda.items():
    print(f"""Nombre: {nombre}
    Telefono: {detalles.get("telefono")}
    Email: {detalles.get("email")}
    Direccion: {detalles.get("direccion")}
""")