# ENTRADA - MATEMÁTICA
exam_mat = float(input("Ingrese la nota del examen de Matemática: "))
A1_mat = float(input("Ingrese la primera nota de tareas de Matemática: "))
A2_mat = float(input("Ingrese la segunda nota de tareas de Matemática: "))
A3_mat = float(input("Ingrese la tercera nota de tareas de Matemática: "))

prom_tareas_mat = (A1_mat + A2_mat + A3_mat) / 3
final_mat = exam_mat * 0.90 + prom_tareas_mat * 0.10

# ENTRADA - FÍSICA
exam_fis = float(input("Ingrese la nota del examen de Física: "))
t1_fis = float(input("Ingrese la primera nota de tareas de Física: "))
t2_fis = float(input("Ingrese la segunda nota de tareas de Física: "))

prom_tareas_fis = (t1_fis + t2_fis) / 2
final_fis = exam_fis * 0.80 + prom_tareas_fis * 0.20

# ENTRADA - QUÍMICA
exam_quim = float(input("Ingrese la nota del examen de Química: "))
t1_quim = float(input("Ingrese la primera nota de tareas de Química: "))
t2_quim = float(input("Ingrese la segunda nota de tareas de Química: "))
t3_quim = float(input("Ingrese la tercera nota de tareas de Química: "))

prom_tareas_quim = (t1_quim + t2_quim + t3_quim) / 3
final_quim = exam_quim * 0.85 + prom_tareas_quim * 0.15

# PROMEDIO GENERAL
promedio_general = (final_mat + final_fis + final_quim) / 3

# SALIDAS
print("---------- RESULTADOS ----------")
print("Promedio final en Matemática:", final_mat)
print("Promedio final en Física:", final_fis)
print("Promedio final en Química:", final_quim)
print("Promedio general de las tres materias:", promedio_general)

