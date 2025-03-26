
suma = 0
k = 1
while suma + (k**2 + 1) / k <= 1000:
    suma += (k**2 + 1) / k
    k += 1
print(f"Número de términos necesarios para aproximarse a 1000 sin excederlo: {k - 1}")
