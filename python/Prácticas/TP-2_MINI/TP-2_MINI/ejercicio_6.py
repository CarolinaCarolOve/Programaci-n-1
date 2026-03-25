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
uso_clave_token =(input("¿Usa clave token?:  SI(a) NO(b) "))#VARIABLE DE ENTRADA 
#DETECTA LOS CARACTERES Y PROCEDE AL PRIMER CONDICIONAL IF 
######################################################################
if uso_clave_token == "a":#ANALIZA QUE EL STRING "a" fue seleccionado
    uso_clave_token==True#En cuyo caso es verdadero el string "a"
    print("Acceso permitido con clave Token")#Imprime un mensaje
else:#En caso de que no se haya tipeado "a", se ha tipeado "b"; b será falso.
    uso_clave_token=="b"
    uso_clave_token==False#Rompe con el mensaje anterior y pasa a otra cosa
    ####################################################################
    #DEFINIMOS QUE EL USUARIO NO USABA TOKEN. ENTONCES PROSEGUIMOS A DECLARAR LAS VARIABLES
    #CLAVE ALMACENADA Y CLAVE INGRESADA SERÁN EMPLEADAS PARA DEFINIR LOS DÍGITOS DE ENTRADA
    clave_almacenada = "1234" #String que me verificará si la clave ingresada es verdadera
    clave_ingresada = input("Ingresar clave: ")#La clave será comparada con el string 

    if clave_almacenada == clave_ingresada:
     print("Acceso permitido") #Imprime este mensaje solo si la clave coincide con el número ingresado por el usuario
    else:
        print ("Acceso denegado")


    

