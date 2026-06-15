#Ejercicio 5  
validador=input("Ingresa el código de materia: ")
if "-" in validador:          
        piezas=validador.split("-")
        letra=piezas[0]
        numero=piezas[1]
        print(f"Código Válido:{validador.upper}")
        if letra.isalpha():
            if numero.isdigit():
                print(f"Codigo valido:{validador.upper()}")
            else:
                print("Error: No hay número")
        else:
            print("Error: No hay letra")
else: 
    print("Error: No hay guión")