Algoritmo EJERCICIO_18_InteresSimple
    
    Escribir "Ingrese el capital prestado (Bol�vares): "
    Leer capital
    Escribir "Ingrese el total de intereses  : "
    Leer interes
    Escribir "Ingrese el tiempo en a�os (por ejemplo, 6): "
    Leer tiempo
    
    razonAnual <- (interes * 100) / (capital * tiempo)
    
    Escribir "------------RESULTADO--------------"
    Escribir "La tasa de interes anual es: ", razonAnual, " %"
FinAlgoritmo