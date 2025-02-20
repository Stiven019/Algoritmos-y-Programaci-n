

# Solicitar los lados del triángulo
a = float(input("Ingrese la longitud del lado a: "))
b = float(input("Ingrese la longitud del lado b: "))
c = float(input("Ingrese la longitud del lado c: "))

# Calcular el semiperímetro
s = (a + b + c) / 2

# Aplicar la fórmula de Herón
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Mostrar el resultado
print(f"El área del triángulo es: {area:.2f}")