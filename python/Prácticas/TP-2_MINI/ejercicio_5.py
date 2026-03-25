#Escribir un programa que determine si un número es:
#- Par o impar
#- Mayor, menor o igual a 10
#Salida esperada:
#El numero es par
#El numero es mayor a 10
numero = float(input("Ingrese un número entero: "))

if numero < 10 and numero%2== 0:
   print(f"El numero {numero} es par")
   print(f"El numero {numero} es menor que 10")
elif numero < 10 and numero%2!=0:
   print(f"El numero {numero} es impar")
   print(f"El numero {numero} es menor que 10")

if numero == 10 and numero%2== 0:
   print(f"El numero {numero} es par")
   print(f"El numero {numero} es igual a 10")
elif numero == 10 and numero%2!=0:
   print(f"El numero {numero} es impar")
   print(f"El numero {numero} es igual a 10")


if numero > 10 and numero%2== 0:
   print(f"El numero {numero} es par")
   print(f"El numero{numero} es mayor que 10")
elif numero > 10 and numero%2!=0:
   print(f"El numero {numero} es impar")
   print(f"El numero{numero} es mayor que 10")

