# ENTRADAS
nombre = input("Ingrese el nombre del trabajador: ")
horas_normales = float(input("Ingrese el número de horas normales trabajadas: "))
pago_hora = float(input("Ingrese el pago por hora normal: "))
horas_extras = float(input("Ingrese el número de horas extras trabajadas: "))
numero_hijos = int(input("Ingrese el número de hijos del trabajador: "))

# PROCESOS
# Sueldo base solo horas normales
sueldo_base = horas_normales * pago_hora

# Pago por horas extras 
pago_horas_extras = horas_extras * pago_hora * 1.25

# Deducciones
deduccion_pago_forzoso = sueldo_base * 0.05
deduccion_politica_habitacional = sueldo_base * 0.02
deduccion_caja_ahorro = sueldo_base * 0.07
total_deducciones = deduccion_pago_forzoso + deduccion_politica_habitacional + deduccion_caja_ahorro

# Asignaciones fijas y por hijo
total_asignaciones = 250000 + (173000 * numero_hijos) + 180000

# Cálculo del sueldo 
sueldo_neto = (sueldo_base + pago_horas_extras) - total_deducciones + total_asignaciones

# SALIDAS
print("---------- RESULTADOS ----------")
print("Trabajador:", nombre)
print("Asignaciones totales:", total_asignaciones, "COP")
print("Deducciones totales:", total_deducciones, "COP")
print("Sueldo neto a recibir:", sueldo_neto, "COP")
