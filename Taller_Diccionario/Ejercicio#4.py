estudiantes = {}
maximo_estudiantes = 10

print("Introduce los datos de los estudiantes:\n")

for i in range(1, maximo_estudiantes + 1):
    nombre = input(f"Nombre del estudiante {i}: ")
    nota = float(input(f"Nota de {nombre}: "))

    estudiantes[str(i)] = {
        "nombre": nombre,
        "nota": nota
    }

aprobados = []
suspendidos = []
suma = 0

for estudiante in estudiantes.values():
    nombre = estudiante["nombre"]
    nota = estudiante["nota"]
    suma += nota

    if nota >= 5:
        aprobados.append(nombre)
    else:
        suspendidos.append(nombre)

# Mostrar resultados
print("\n--- RESULTADOS ---")
print("Aprobados:", ", ",aprobados)
print("Suspendidos:", ", ",suspendidos)
print(f"Nota media de la clase: {suma / maximo_estudiantes:.2f}")