# ENTRADA
horas = float(input("Horas trabajadas: "))
precio = float(input("Precio de la hora: "))

# PROCESO
salario = horas * precio
descuento = salario * 0.20
sueldo_total = salario - descuento

# SALIDA
print("Salario base es:", salario)
print("Descuento por impuestos:", descuento)
print("El salario neto es:", sueldo_total)
