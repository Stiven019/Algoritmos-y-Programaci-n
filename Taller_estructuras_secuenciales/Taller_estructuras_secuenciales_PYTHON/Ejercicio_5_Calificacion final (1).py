# ENTRADA
parcial1 = int(input("Ingrese la primera calificación parcial: "))
parcial2 = int(input("Ingrese la segunda calificación parcial: "))
parcial3 = int(input("Ingrese la tercera calificación parcial: "))
examen_final = int(input("Ingrese la calificación del examen final: "))
trabajo_final = int(input("Ingrese la calificación del trabajo final: "))

# PROCESO
promedio_parciales = (parcial1 + parcial2 + parcial3) / 3
calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)

# SALIDA
print("      RESULTADO")
print("La calificación final es:", calificacion_final)
