
N = int(input("Ingrese un número de 4 dígitos: "))
centenas = (N // 100) * 100
if N % 100 >= 50:
    N = centenas + 100
else:
    N = centenas
print(f"Número redondeado: {N}")
