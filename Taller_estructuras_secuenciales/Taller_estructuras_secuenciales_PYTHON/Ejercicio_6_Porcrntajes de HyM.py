# ENTRADA
mujeres = int(input("Número de mujeres: "))
hombres = int(input("Número de hombres: "))

# PROCESO
total_estudiantes = mujeres + hombres
porcentaje_mujeres = (mujeres / total_estudiantes) * 100
porcentaje_hombres = (hombres / total_estudiantes) * 100

# SALIDA

print("       RESULTADO")
print("Porcentaje de hombres:", porcentaje_hombres, "%")
print("Porcentaje de mujeres:", porcentaje_mujeres, "%")

