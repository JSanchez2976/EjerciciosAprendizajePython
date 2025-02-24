nombre = input("Nombre: ")
pasos_caminados =int(input("Pasos caminados: "))

meta_pasos_diarios = 400
calorias_por_paso = 0.04

calorias_quemadas = pasos_caminados*calorias_por_paso
meta_alcanzada= pasos_caminados >= meta_pasos_diarios

print("-------------------------")
if meta_alcanzada:
    print("Enhorabuena, has alcanzado la meta")
    print(f"Calorias quemadas: {calorias_quemadas}")
else:
    print("Una pena, no has alcanzado la meta")
    print(f"Calorias quemadas: {calorias_quemadas}")