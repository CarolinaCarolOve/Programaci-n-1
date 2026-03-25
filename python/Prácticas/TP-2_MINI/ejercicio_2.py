##Ejercicio 2
##Diseñar un algoritmo que indique qué ropa usar según la temperatura.
#Datos:Temperaturas
#Condiciones:
#- Menor a 10: abrigo
#- Entre 10 y 20: ropa media
#- Mayor a 20: ropa liviana
clima = int(input ("Introduce tu clima en grados centígrados: "))
#El usuario ingresó un número de tipo entero que corresponde al clima
#La variable clima lee este dato
if clima < 10:#lee que el clima corresponda a menos de 10 grados
    print("Usar ropa de abrigo")#acá imprimiría la recomendación 
    #correspondiente en caso de que el clima sea menor a 10 grados
elif 10<clima<20:#Clima verifica que el dato del clima ingresado es mayor que 10 grados pero menor a 20 grados
    print("Usar ropa media")#imprime un mensaje que con la recomendación pertinente
else: #Utilizo un else para que lea los demás datos, que no corresponden a ninguno de los otros dos
#Es decir, que no sean menores que 10, pero tampoco son menores que 20, solo son los mayores a 20 grados centígrados
   print("Usar ropa liviana")#brinda la recomendación para esos casos donde el clima es mayor que 20
   




