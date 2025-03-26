
saldo = 1000  # Saldo inicial
    
while True:
    print("\n--- Cajero Automático ---")
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Salir")
        
    opcion = input("Seleccione una opción: ")
        
    if opcion == "1":
        monto = float(input("Ingrese el monto a depositar: "))
        if monto > 0:
            saldo += monto
            print(f"Depósito exitoso. Su nuevo saldo es: ${saldo:.2f}")
        else:
            print("El monto debe ser positivo.")
                
    elif opcion == "2":
        monto = float(input("Ingrese el monto a retirar: "))
        if monto > 0:
            if monto <= saldo:
                saldo -= monto
                print(f"Retiro exitoso. Su nuevo saldo es: ${saldo:.2f}")
            else:
                print("Saldo insuficiente.")
        else:
            print("El monto debe ser positivo.")
                
    elif opcion == "3":
        print(f"Su saldo actual es: ${saldo:.2f}")
            
    elif opcion == "4":
        print("Gracias por usar el cajero automático. Hasta luego!")
        break
        
    else:
        print("Opción no válida. Intente de nuevo.")