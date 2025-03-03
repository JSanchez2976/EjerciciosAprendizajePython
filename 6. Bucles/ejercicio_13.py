# Break y continue

# Ejemplo break
print("Ejemplo break: ")
for numero in range(1,10):
    if numero %2 == 0:
        print(numero)
        break # Salir del bucle

# Ejemplo continue
print("Ejemplo continue: ")
for numero in range(1,10):
    if numero %2 == 1: # numero impar
        continue
    print(numero) # numeros pares