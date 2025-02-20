# ENTRADA
chelines = float(input("Ingrese la cantidad en chelines austriacos: "))
pesetas_de_chelines = chelines * 9.56871
print("Equivalente en pesetas:", pesetas_de_chelines)
print()

dracmas = float(input("Ingrese la cantidad en dracmas griegos: "))
pesetas_de_dracmas = dracmas * 0.88607
francos = pesetas_de_dracmas / 20.110
print("Equivalente en francos franceses:", francos)
print()

pesetas_ingresadas = float(input("Ingrese la cantidad en pesetas: "))
dolares = pesetas_ingresadas / 122.499
liras = pesetas_ingresadas * 10.763

# SALIDA
print("Equivalente en dólares:", dolares)
print("Equivalente en liras italianas:", liras)
