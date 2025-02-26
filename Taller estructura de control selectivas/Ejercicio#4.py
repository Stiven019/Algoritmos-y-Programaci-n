
monto = float(input("Ingrese el monto total de la compra: "))
if monto > 5000000:
    inversion = monto * 0.55
    prestamo_banco = monto * 0.30
    credito_fabricante = monto * 0.15
else:
    inversion = monto * 0.70
    prestamo_banco = 0
    credito_fabricante = monto * 0.30
intereses = credito_fabricante * 0.20
print(f"Inversión: {inversion}, Crédito: {credito_fabricante}, Intereses: {intereses}, Préstamo: {prestamo_banco}")
