import math
# ENTRADA
metros = float(input("Cantidad en metros: "))

# PROCESO
pulgadas_totales = metros * 39.27
pies = math.trunc(pulgadas_totales / 12)
pulgadas = pulgadas_totales - (pies * 12)

# SALIDA
print("La cantidad equivale a:", pies, "pies y", pulgadas, "pulgadas")
 