def tiene_anemia(edad, sexo, hemoglobina):
    if edad <= 1:  # 0 meses a 1 mes
        minimo = 13
    elif 1 < edad <= 6:  # Mayor de 1 mes y hasta 6 meses
        minimo = 10
    elif 6 < edad <= 12:  # Mayor de 6 meses y hasta 12 meses
        minimo = 11
    elif 1 < edad <= 5:  # Mayor de 1 año y hasta 5 años
        minimo = 11.5
    elif 5 < edad <= 10:  # Mayor de 5 años y hasta 10 años
        minimo = 12.6
    elif 10 < edad <= 15:  # Mayor de 10 años y hasta 15 años
        minimo = 13
    elif edad > 15:  
        if sexo.lower() == "mujer":
            minimo = 12
        elif sexo.lower() == "hombre":
            minimo = 14
        else:
            return "Sexo no válido"
    else:
        return "Edad no válida"

    return "Tiene anemia" if hemoglobina < minimo else "No tiene anemia"

# Entrada de datos
edad = float(input("Ingrese la edad en años: "))
sexo = input("Ingrese el sexo (hombre/mujer): ")
hemoglobina = float(input("Ingrese el nivel de hemoglobina (g%): "))

# Salida de datos
resultado = tiene_anemia(edad, sexo, hemoglobina)
print(resultado)

