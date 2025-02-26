def calcular_costo_alquiler(km_recorridos):
    if km_recorridos <= 300:
        return 50000  # Tarifa fija si no supera los 300 km
    elif km_recorridos <= 1000:
        costo_base = 70000
        km_extra = km_recorridos - 300
        return costo_base + (km_extra * 30000)
    else:
        costo_base = 150000
        km_extra = km_recorridos - 1000
        return costo_base + (km_extra * 9000)

# Entrada de datos
km_recorridos = float(input("Ingrese la cantidad de kilómetros recorridos: "))
costo_total = calcular_costo_alquiler(km_recorridos)

# Salida de datos
print(f"El total a pagar por el alquiler es: {costo_total:,} COP")