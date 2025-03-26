
print("Números impares menores que 100 (excepto los divisibles por 7):")
for i in range(1, 100, 2):
    if i % 7 != 0:
        print(i)