nombre = input("Ingrese el nombre del cliente: ")
monto_compra = float(input("Ingrese el monto de la compra: "))

# Determinar el descuento
if monto_compra < 50000:
    descuento = 0
elif monto_compra <= 100000:
    descuento = 0.05
elif monto_compra <= 700000:
    descuento = 0.11
elif monto_compra <= 1500000:
    descuento = 0.18
else:
    descuento = 0.25

# Calcular el monto a pagar
descuento_aplicado = monto_compra * descuento
monto_a_pagar = monto_compra - descuento_aplicado

# Mostrar resultados
print("Cliente: " + nombre)
print("Monto de la compra: $" + str(monto_compra))
print("Descuento recibido: $" + str(descuento_aplicado))
print("Monto a pagar: $" + str(monto_a_pagar))
