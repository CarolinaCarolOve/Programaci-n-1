#Datos:
#-Clave almacenada
#-Clave_ingresada
#-Usa_token("True"o "false")
# CONDICIÓN:
# -Permitir acceso si la clave es incorrecta
# o si el usuario usa token
# SALIDA: 
# - "Acceso permitido"
# -"Acceso denegado"
uso_clave_token =(input("¿Usa clave token?:  SI(a) NO(b) "))
if uso_clave_token == "a":
    uso_clave_token==True
    print("Acceso permitido con clave Token")

else:
    uso_clave_token=="b"
    uso_clave_token==False


    clave_almacenada = "1234" #String que me verificará si la clave ingresada es verdadera
    clave_ingresada = input("Ingresar clave: ")#La clave será comparada con el string 

    if clave_almacenada == clave_ingresada:
     print("Acceso permitido") #Imprime este mensaje solo si la clave coincide con el número ingresado por el usuario
    else:
        print ("Acceso denegado")
        

    

