
ventas1 = float(input("Ingrese las ventas del departamento 1: "))
ventas2 = float(input("Ingrese las ventas del departamento 2: "))
ventas3 = float(input("Ingrese las ventas del departamento 3: "))
ventas_totales = ventas1 + ventas2 + ventas3
salario = float(input("Ingrese el salario mensual de un vendedor: "))

for ventas in [ventas1, ventas2, ventas3]:
    if ventas > ventas_totales * 0.33:
        print(f"Salario con incentivo: {salario * 1.20}")
    else:
        print(f"Salario sin incentivo: {salario}")
