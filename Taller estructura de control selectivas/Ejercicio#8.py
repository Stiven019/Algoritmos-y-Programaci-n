P = int(input("Ingrese el valor de P: "))
Q = int(input("Ingrese el valor de Q: "))

# Evaluamos la expresión
expresion = (P**3 + Q**4 - 2 * P**2) > 680

# Mostramos el resultado
if expresion:
    print("P = " + str(P) + " y Q = " + str(Q) + " satisfacen la expresión.")
else:
    print("P = " + str(P) + " y Q = " + str(Q) + " no satisfacen la expresión.")