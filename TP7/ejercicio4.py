edad= ((input("Ingresa tu edad: ")))
if edad.strip().isnumeric():
    eedad = int(edad)
    if 0< eedad <120:
        print(f"Edad registrada:{edad}")
    else: 
        print("Error, el dato ingresado no ha sido validado")
else: 
    print("Ingresa un número válido")
    
 
