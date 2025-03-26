def es_numero_perfecto(numero):
    suma_divisores = sum(i for i in range(1, numero) if numero % i == 0)
    return suma_divisores == numero

def verificar_numero_perfecto():
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero <= 0:
            print("Por favor, ingrese un número positivo.")
            return
        
        if es_numero_perfecto(numero):
            print(f"{numero} es un número perfecto.")
        else:
            print(f"{numero} no es un número perfecto.")
    except ValueError:
        print("Entrada inválida. Ingrese un número entero positivo.")


