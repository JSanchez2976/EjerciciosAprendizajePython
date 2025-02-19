nombre = "Jorge Sanchez Aldana"
colegio = "Colegio Montessori"
dominio = ".com"

email = nombre.replace(" ",".").lower()+"@"+colegio.lower().replace(" ","")+dominio

print(email)