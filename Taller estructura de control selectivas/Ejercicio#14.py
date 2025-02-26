def calcular_pago(l_anterior, l_actual):
    consumo = l_actual - l_anterior
    total = 0
    
    if consumo <= 100:
        total = consumo * 4_600
    elif consumo <= 300:
        total = (100 * 4_600) + ((consumo - 100) * 80_000)
    elif consumo <= 500:
        total = (100 * 4_600) + (200 * 80_000) + ((consumo - 300) * 100_000)
    else:
        total = (100 * 4_600) + (200 * 80_000) + (200 * 100_000) + ((consumo - 500) * 120_000)

    return total

# Solicitar datos al usuario
lectura_anterior = int(input("Ingrese la lectura anterior del medidor (Kwh): "))
lectura_actual = int(input("Ingrese la lectura actual del medidor (Kwh): "))

# Calcular el monto a pagar
monto_a_pagar = calcular_pago(lectura_anterior, lectura_actual)

# Mostrar el resultado
print(f"El monto total a pagar es: {monto_a_pagar:,} COP")

