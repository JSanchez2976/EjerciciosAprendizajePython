# Prestamo libros

distancia_permitida_km = 3
tiene_credencial = input(f'Tienes credencial de estudiante: ')
distancia_biblioteca = int(input(f'A cuantos km vives: '))

es_elegible = (tiene_credencial.strip().lower() =="si"
               or distancia_biblioteca <= distancia_permitida_km)
print(f'Es elegible: {es_elegible}')