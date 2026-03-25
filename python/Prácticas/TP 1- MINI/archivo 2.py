#IF ELIF ElSE
#Armamos nuevamente el mismo código implementando elif y else. 
clave_almacenada = "1234" #String que me verificará si la clave ingresada es verdadera
clave_ingresada = input("Ingresar clave: ")#La clave será comparada con el string 
uso_clave_token = bool(input("¿Usa clave token?: SI(a) NO(b)")== "a") #Determina que cualquier uso de clave toekn queda descartada y es falsa

if clave_almacenada == clave_ingresada: #compara ambas variables, el número ue ingresa el usuario y la clave verdadera
    print("Acceso con clave") #Imprime este mensaje solo si la clave coincide con el número ingresado por el usuario
elif uso_clave_token == "a":
    print ("Acceso permitido con clave Token", False)
else:
    print ("Acceso denegado")
    