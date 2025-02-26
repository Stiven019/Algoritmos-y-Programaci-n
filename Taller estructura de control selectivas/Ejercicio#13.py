def desglosar_cantidad(cantidad):
    billetes_monedas = [
        100000, 50000, 20000, 10000, 5000, 2000, 1000,
        500, 200, 100, 50
    ]
    cantidad = cantidad // 50 * 50  # Redondear para ignorar unidades menores a 50
    desglose = []
    
    for valor in billetes_monedas:
        if cantidad >= valor:
            cantidad_unidades = cantidad // valor
            cantidad -= cantidad_unidades * valor
            desglose.extend([valor] * cantidad_unidades)
    
    return desglose

# Ejemplo de uso
cantidad = int(input("Ingrese la cantidad en COP: "))
resultado = desglosar_cantidad(cantidad)
print(", ".join(map(str, resultado)))
