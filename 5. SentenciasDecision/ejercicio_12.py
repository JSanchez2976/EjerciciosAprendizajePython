# Sistema de envios

destino = input("Destino (nacional/internacional): ").strip().lower()
kilos = int(input("Kilos= "))

COSTE_NACIONAL= 10 * kilos
COSTE_INTERNACINAL=20 * kilos

if destino == 'nacional':
    print(f"Envio {destino}, total = {COSTE_NACIONAL}€")
elif destino == 'internacional':
    print(f"Envio {destino}, total = {COSTE_INTERNACINAL}€")
else:
    print("Introduce nacional o internacional")