estudiantes = []
puntajes = []
    
while True:
    nombre = input("Ingrese el nombre del estudiante (o 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
        
    try:
        puntaje = float(input(f"Ingrese el puntaje de {nombre}: "))
        estudiantes.append(nombre)
        puntajes.append(puntaje)
    except ValueError:
        print("Por favor, ingrese un puntaje válido.")
    
if not puntajes:
    print("No se ingresaron datos.")
    
max_puntaje = max(puntajes)
min_puntaje = min(puntajes)
nombre_max = estudiantes[puntajes.index(max_puntaje)]
nombre_min = estudiantes[puntajes.index(min_puntaje)]
promedio = sum(puntajes) / len(puntajes)
    
inferiores = sum(1 for p in puntajes if p < promedio) / len(puntajes) * 100
superiores = sum(1 for p in puntajes if p > promedio) / len(puntajes) * 100
    
print("\nResultados:")
print(f"Estudiante con el puntaje más alto: {nombre_max} ({max_puntaje})")
print(f"Estudiante con el puntaje más bajo: {nombre_min} ({min_puntaje})")
print(f"Puntaje máximo obtenido: {max_puntaje}")
print(f"Puntaje mínimo obtenido: {min_puntaje}")
print(f"Promedio de puntajes: {promedio:.2f}")
print(f"Porcentaje de estudiantes con puntajes inferiores al promedio: {inferiores:.2f}%")
print(f"Porcentaje de estudiantes con puntajes superiores al promedio: {superiores:.2f}%")
