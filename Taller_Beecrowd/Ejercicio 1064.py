# Inicializar lista para guardar los números positivos
positivos = []

for _ in range(6):
    valor = float(input())
    if valor > 0:
        positivos.append(valor)


cantidad_positivos = len(positivos)
promedio = sum(positivos) / cantidad_positivos


print(f"{cantidad_positivos} valores positivos")
print(f"{promedio:.1f}")

