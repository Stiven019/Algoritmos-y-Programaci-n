
while True:
        consume = input("¿Consume licor? (Sí/No): ").strip().lower()
        if consume == "sí":
            total_consumidores += 1
            licor = int(input("Licor preferido (1-Aguardiente, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro): "))
        else:
            licor = None
        
        edad = int(input("Ingrese su edad: "))
        sexo = input("Ingrese su sexo (M/F): ").strip().upper()
        
        if sexo == "F" and edad < 18:
            mujeres_menores += 1
        
        if sexo == "M" and licor != 1 and 20 <= edad <= 25:
            hombres_sin_aguardiente += 1
        
        if licor == 3:
            total_cerveza += 1
            suma_edades_cerveza += edad
        
        if licor == 5:
            total_whisky += 1
            total_encuestados += 1
        
        continuar = input("¿Desea continuar con la encuesta? (Sí/No): ").strip().lower()
        if continuar != "sí":
            break
    
promedio_cerveza = suma_edades_cerveza / total_cerveza if total_cerveza > 0 else 0
porcentaje_whisky = (total_whisky / total_encuestados) * 100 if total_encuestados > 0 else 0
    
print(f"Total de personas que consumen licor: {total_consumidores}")
print(f"Total de mujeres menores de edad: {mujeres_menores}")
print(f"Total de hombres entre 20 y 25 años que no consumen aguardiente: {hombres_sin_aguardiente}")
print(f"Promedio de edad de quienes consumen cerveza: {promedio_cerveza:.2f}")
print(f"Porcentaje de personas que consumen whisky respecto al total: {porcentaje_whisky:.2f}%")
