cantidad = int(input("Ingrese la cantidad en COP: "))

billetes_monedas = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50]
resultado = []

for valor in billetes_monedas:
    cantidad_billetes = cantidad // valor
    if cantidad_billetes > 0:
        resultado.append(f"{cantidad_billetes} x {valor}")
        cantidad %= valor

print("Desglose: " + ", ".join(resultado))