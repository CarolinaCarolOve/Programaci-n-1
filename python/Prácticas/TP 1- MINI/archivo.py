#Condicionales-condicional "if"
####################################################################################################
#La traducción de if es "si" en español, imaginemos el acceso al banco verificando nuestra contraseña. 
password_ingresada = input("Introducir contraseña: ")
password_almacenada = "12345"
acceso_permitido = False #devuelve un dato booleano que verifica un criterio de falsedad############
####################################################################################################
if password_almacenada == password_ingresada: #condición lógica#####################################
        acceso_permitido = True ##bloque condicionado ##############################################
        print("Acceso permitido")
        print("gracias por usar el acceso seguro del banco")
if password_almacenada != password_ingresada:
     acceso_permitido = False
     print("acceso denegado")
     print("Gracias por usar el acceso seguro del banco")
        
        
    