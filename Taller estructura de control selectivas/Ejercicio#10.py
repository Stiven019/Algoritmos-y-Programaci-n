# Solicitar sueldo del trabajador
salario_bruto = float(input("Ingrese el sueldo bruto del trabajador: "))

# Determinar categoría y aumento según el sueldo bruto
if salario_bruto == 5000000:
    aumento = 0.10
    categoria = 1
elif salario_bruto == 4300000:
    aumento = 0.15
    categoria = 2
elif salario_bruto == 3600000:
    aumento = 0.20
    categoria = 3
elif salario_bruto == 2000000:
    aumento = 0.40
    categoria = 4
elif salario_bruto == 900000:
    aumento = 0.60
    categoria = 5
else:
    aumento = 0
    categoria = "No definida"
    print("Sueldo no corresponde a ninguna categoría predefinida.")

# Calcular nuevo sueldo bruto
nuevo_sueldo = salario_bruto + (salario_bruto * aumento)

# Mostrar resultado
print("Categoría del trabajador: " + str(categoria))
print("Nuevo sueldo bruto: $" + str(nuevo_sueldo))