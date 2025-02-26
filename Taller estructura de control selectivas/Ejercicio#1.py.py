Ejercicio#1

# Solicitar datos al usuario
capital = float(input("Ingrese el monto de inversión inicial (COP): "))
tasa_interes = float(input("Ingrese la tasa de interés anual (%): ")) / 100
tiempo = int(input("Ingrese el número de años: "))

# Calcular los intereses generados
interes_generado = capital * tasa_interes * tiempo

# Decisión sobre la reinversión
if interes_generado > 100000:
    monto_final = capital + interes_generado
    print(f"Los intereses generados son: ${interes_generado:,.2f} COP")
    print(f"Como los intereses superan $100,000 COP, se reinvertirán.")
    print(f"Monto final en la cuenta: ${monto_final:,.2f} COP")
else:
    print(f"Los intereses generados son: ${interes_generado:,.2f} COP")
    print(f"Como los intereses no superan $100,000 COP, no se reinvertirán.")
    print(f"Monto final en la cuenta: ${capital:,.2f} COP")

