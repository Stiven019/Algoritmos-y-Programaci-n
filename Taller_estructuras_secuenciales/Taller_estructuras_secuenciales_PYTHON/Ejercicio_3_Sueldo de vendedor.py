# ENTRADA
sueldo_base = int(input("Ingrese el sueldo base del vendedor: "))
venta1 = int (input("Ingrese el monto de la primera venta: "))
venta2 = int (input("Ingrese el monto de la segunda venta: "))
venta3 = int (input("Ingrese el monto de la tercera venta: "))

# PROCESO
comision = (venta1 + venta2 + venta3) * 0.10
total = sueldo_base + comision

# SALIDA
print("El total de comisiones es:", comision)
print("El sueldo total del vendedor es:", total)
